# 🚗 ParkEasy - Parking Slot Booking System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple.svg)](https://getbootstrap.com/)

> A modern, cinema-style parking slot booking system built with Flask and inspired by BookMyShow's elegant UI design.

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

ParkEasy is a sophisticated parking slot booking system that provides an intuitive, cinema-style interface for reserving parking spaces. The system features three distinct parking categories with dynamic pricing, real-time availability updates, and a premium user experience designed to rival modern booking platforms.

### Key Highlights

- 🎨 **BookMyShow-inspired UI** - Dark theme with gradient effects and smooth animations
- 🏷️ **Three-tier pricing system** - VIP (₹500), Executive (₹350), and Normal (₹320) categories
- 💰 **Dynamic fee structure** - Static platform fee (₹18) and night surcharge (₹12)
- 📱 **Responsive design** - Optimized for desktop, tablet, and mobile devices
- ⚡ **Real-time updates** - Instant booking confirmations and availability status
- 🔄 **RESTful API** - Clean API endpoints for integration and automation

## ✨ Features

### 🎪 Booking Experience
- **Visual slot selection** with cinema-style layout
- **Multi-category booking** in a single transaction
- **Real-time pricing calculator** with fee breakdown
- **Interactive slot map** with hover effects and animations
- **Booking confirmation modal** with detailed receipt

### 💳 Pricing & Fees
- **Base parking rates**: VIP (₹500), Executive (₹350), Normal (₹320)
- **Platform fee**: Fixed ₹18 charge
- **Night surcharge**: Additional ₹12 for bookings between midnight and 5 AM
- **Transparent billing** with itemized cost breakdown

### 🎨 User Interface
- **Dark gradient theme** with glass-morphism effects
- **Color-coded categories** for easy identification
- **Smooth animations** and micro-interactions
- **Professional typography** and spacing
- **Accessibility-friendly** design patterns

### 🔧 Technical Features
- **JSON-based data persistence** for development
- **Error handling** with graceful fallbacks
- **API-first architecture** for easy integration
- **Responsive grid system** for optimal viewing
- **Cross-browser compatibility**

## 🎬 Demo

### Screenshots

#### Home Page
Modern landing page with category selection cards featuring hover effects and gradient backgrounds.

#### Booking Interface
Cinema-style slot selection with real-time pricing and booking summary panel.

#### Confirmation Modal
Professional booking confirmation with detailed pricing breakdown and receipt.

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/parkeasy.git
   cd parkeasy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

### Development Setup

For development with hot reloading:

```bash
# Set Flask environment variables
export FLASK_ENV=development
export FLASK_DEBUG=1

# Run the application
python app.py
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Flask environment mode | `development` |
| `FLASK_DEBUG` | Enable debug mode | `True` |
| `SECRET_KEY` | Flask session secret key | `your-secret-key-here` |

### Pricing Configuration

Update pricing in `app.py`:

```python
parking_data = {
    'vip': {'price': 500},      # VIP parking rate
    'executive': {'price': 350}, # Executive parking rate
    'normal': {'price': 320}     # Normal parking rate
}

# Fee structure
PLATFORM_FEE = 18              # Static platform fee
NIGHT_SURCHARGE = 12           # Night time surcharge
```

## 📚 API Documentation

### Endpoints

#### `GET /`
**Home page** - Landing page with parking category overview

#### `GET /select-seats`
**Booking interface** - Main slot selection and booking page

#### `GET /parking`
**Parking overview** - Complete parking layout view

#### `GET /api/parking-status`
**Get parking status** - Returns current slot availability

**Response:**
```json
{
  "vip": {
    "price": 500,
    "slots": ["V1", "V2", ...],
    "booked": ["V1"]
  },
  "executive": { ... },
  "normal": { ... }
}
```

#### `POST /api/book-slots`
**Book parking slots** - Reserve selected slots

**Request:**
```json
{
  "type": "vip",
  "slots": ["V1", "V2"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Successfully booked 2 slots",
  "booked_slots": ["V1", "V2"],
  "pricing": {
    "base_amount": 1000,
    "platform_fee": 18,
    "night_surcharge": 0,
    "grand_total": 1018
  }
}
```

#### `POST /api/calculate-fees`
**Calculate fees** - Get pricing breakdown for given amount

**Request:**
```json
{
  "base_amount": 1000
}
```

**Response:**
```json
{
  "base_amount": 1000,
  "platform_fee": 18,
  "night_surcharge": 12,
  "total_fees": 30,
  "grand_total": 1030,
  "is_night_time": true
}
```

#### `GET /api/time-info`
**Time information** - Get current time and night surcharge status

## 📁 Project Structure

```
parkeasy/
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
├── 📄 parking_data.json     # Booking data storage
├── 📁 templates/            # Jinja2 HTML templates
│   ├── 📄 index.html        # Home page template
│   ├── 📄 select_seats.html # Booking interface
│   └── 📄 parking.html      # Parking overview
├── 📁 static/               # Static assets
│   └── 📁 css/
│       └── 📄 style.css     # Custom stylesheets
└── 📁 docs/                 # Documentation assets
    └── 📁 screenshots/      # UI screenshots
```

## 🛠️ Technologies Used

### Backend
- **[Flask](https://flask.palletsprojects.com/)** - Python web framework
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** - WSGI web application library
- **JSON** - Data persistence for development

### Frontend
- **[Bootstrap 5](https://getbootstrap.com/)** - CSS framework
- **[JavaScript ES6+](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Client-side scripting
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Custom styling and animations
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)** - Semantic markup

### UI/UX Design
- **Glass-morphism effects** for modern appearance
- **CSS Grid & Flexbox** for responsive layouts
- **CSS animations** for smooth interactions
- **Color theory** for visual hierarchy

## 🤝 Contributing

We welcome contributions to ParkEasy! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Use semantic commit messages
- Add tests for new features
- Update documentation for API changes
- Ensure responsive design for all screen sizes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BookMyShow** - UI/UX inspiration for the booking interface
- **Flask Community** - Excellent documentation and support
- **Bootstrap Team** - Responsive framework foundation
- **Contributors** - Everyone who helped improve this project

---

<div align="center">
  <p>Built with ❤️ using Flask and modern web technologies</p>
  <p>
    <a href="#top">Back to top ⬆️</a>
  </p>
</div>

---

> **Note:** This project is intended for educational and demonstration purposes. For production deployment, consider implementing a robust database solution and additional security measures.