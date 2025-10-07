from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Fee calculation functions
def calculate_platform_fee(base_amount):
    """Calculate static platform fee of ₹18"""
    return 18

def is_midnight_to_5am():
    """Check if current time is between midnight (00:00) and 5:00 AM"""
    current_hour = datetime.now().hour
    return 0 <= current_hour < 5

def calculate_night_surcharge(base_amount):
    """Calculate static night surcharge of ₹12 for midnight to 5 AM bookings"""
    if is_midnight_to_5am():
        return 12
    return 0

def calculate_total_fees(base_amount):
    """Calculate all fees and return breakdown"""
    platform_fee = calculate_platform_fee(base_amount)
    night_surcharge = calculate_night_surcharge(base_amount)
    
    fees = {
        'base_amount': base_amount,
        'platform_fee': platform_fee,
        'night_surcharge': night_surcharge,
        'total_fees': platform_fee + night_surcharge,
        'grand_total': base_amount + platform_fee + night_surcharge,
        'is_night_time': is_midnight_to_5am()
    }
    
    return fees

# Initialize parking slots data
def initialize_parking_data():
    parking_data = {
        'vip': {
            'price': 500,
            'slots': ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10'],
            'booked': []
        },
        'executive': {
            'price': 350,
            'slots': [],
            'booked': []
        },
        'normal': {
            'price': 320,
            'slots': ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11'],
            'booked': []
        }
    }
    
    # Generate executive slots (larger section)
    for row in range(1, 6):  # 5 rows
        for col in range(1, 21):  # 20 columns
            parking_data['executive']['slots'].append(f'E{row:02d}{col:02d}')
    
    return parking_data

# Load or create parking data
def load_parking_data():
    if os.path.exists('parking_data.json'):
        with open('parking_data.json', 'r') as f:
            return json.load(f)
    else:
        data = initialize_parking_data()
        save_parking_data(data)
        return data

def save_parking_data(data):
    with open('parking_data.json', 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parking')
def parking():
    parking_data = load_parking_data()
    return render_template('parking.html', parking_data=parking_data)

@app.route('/api/parking-status')
def parking_status():
    parking_data = load_parking_data()
    return jsonify(parking_data)

@app.route('/api/book-slots', methods=['POST'])
def book_slots():
    data = request.get_json()
    slot_type = data.get('type')
    slots = data.get('slots', [])
    
    if not slot_type or not slots:
        return jsonify({'success': False, 'message': 'Invalid booking data'})
    
    parking_data = load_parking_data()
    
    # Check if slots are available
    for slot in slots:
        if slot in parking_data[slot_type]['booked']:
            return jsonify({'success': False, 'message': f'Slot {slot} is already booked'})
    
    # Book the slots
    parking_data[slot_type]['booked'].extend(slots)
    save_parking_data(parking_data)
    
    # Calculate pricing with fees
    base_price = len(slots) * parking_data[slot_type]['price']
    fee_breakdown = calculate_total_fees(base_price)
    
    return jsonify({
        'success': True, 
        'message': f'Successfully booked {len(slots)} slots',
        'booked_slots': slots,
        'pricing': fee_breakdown
    })

@app.route('/api/calculate-fees', methods=['POST'])
def calculate_fees():
    """API endpoint to calculate fees for frontend display"""
    data = request.get_json()
    base_amount = data.get('base_amount', 0)
    
    fee_breakdown = calculate_total_fees(base_amount)
    
    return jsonify(fee_breakdown)

@app.route('/select-seats')
def select_seats():
    parking_data = load_parking_data()
    return render_template('select_seats.html', parking_data=parking_data)

@app.route('/test-fees')
def test_fees():
    """Test page for fee calculation"""
    return render_template('test_fees.html')

@app.route('/api/time-info')
def time_info():
    """API endpoint to get current time info for testing"""
    current_time = datetime.now()
    return jsonify({
        'current_hour': current_time.hour,
        'current_time': current_time.strftime('%H:%M'),
        'is_night_time': is_midnight_to_5am(),
        'night_surcharge_applies': is_midnight_to_5am()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)