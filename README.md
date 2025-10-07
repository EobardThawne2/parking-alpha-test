# Parking Slot Booking Website

A Flask-based parking slot booking system with an intuitive UI for selecting and booking parking spaces.

## Features

- **Three Parking Categories:**
  - VIP Parking (₹500) - Premium slots with valet service
  - Executive Parking (₹350) - Covered parking with security
  - Normal Parking (₹320) - Standard parking slots

- **Interactive Booking Interface:**
  - Visual slot selection similar to cinema booking
  - Real-time availability updates
  - Multiple slot selection
  - Booking confirmation system

- **Responsive Design:**
  - Mobile-friendly interface
  - Bootstrap-based UI
  - Modern and clean design

## Installation

1. Make sure you have Python installed on your system
2. Install Flask:
   ```
   pip install flask
   ```

3. Navigate to the project directory:
   ```
   cd "c:\Users\admin\Desktop\PARKING"
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and go to: `http://127.0.0.1:5000`

## Usage

1. **Home Page:** Choose your preferred parking category
2. **Slot Selection:** Click on available slots to select them
3. **Booking:** Confirm your selection and complete the booking
4. **View All Slots:** See the complete parking layout and availability

## File Structure

```
PARKING/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Home page
│   ├── select_seats.html # Slot selection interface
│   └── parking.html      # All slots overview
├── static/
│   └── css/
│       └── style.css     # Styling
├── parking_data.json     # Booking data (auto-generated)
└── README.md            # This file
```

## API Endpoints

- `GET /` - Home page
- `GET /parking` - View all parking slots
- `GET /select-seats?type={vip|executive|normal}` - Slot selection page
- `GET /api/parking-status` - Get current parking status (JSON)
- `POST /api/book-slots` - Book selected slots (JSON)

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5
- **Data Storage:** JSON file

## License

This project is open source and available under the MIT License.