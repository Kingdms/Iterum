# Appliance Asset Management Solution

This project implements an appliance asset management solution for property managers to view recommended appliance replacement options and schedule deliveries.

## Project Structure

The project is divided into two main parts:

1. **Backend**: A Django REST API that provides endpoints for managing properties, flats, appliances, replacement options, and orders.
2. **Frontend**: A web interface built with HTML, CSS, and JavaScript that consumes the API.

## Features

- View recommended appliance replacement options
- Compare different replacement appliances (brand, price, specifications)
- Order replacement appliances
- Schedule delivery of selected appliances

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd appliance_manager/backend
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install django djangorestframework django-cors-headers psycopg2-binary
   ```

4. Run migrations:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Populate the database with initial data:
   ```
   python3 manage.py populate_db
   ```

6. Start the Django development server:
   ```
   python3 manage.py runserver
   ```

The backend API will be available at http://localhost:8000/api/

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd appliance_manager/frontend
   ```

2. Start the frontend server:
   ```
   python3 server.py
   ```

The frontend will be available at http://localhost:8080

## API Endpoints

- `GET /api/properties/`: List all properties
- `GET /api/flats/`: List all flats
- `GET /api/appliances/`: List all appliances
- `GET /api/replacement-options/`: List all replacement options
- `GET /api/appliances/{id}/replacement-options/`: Get replacement options for a specific appliance
- `POST /api/orders/`: Create a new order
- `GET /api/orders/`: List all orders

## Data Schema

The application uses the following data models:

1. **Property**: Represents a property (e.g., Blackhorse Mills)
2. **Flat**: Represents a flat within a property (e.g., Flat 101)
3. **Appliance**: Represents an appliance within a flat
4. **ReplacementOption**: Represents a replacement option for an appliance
5. **Order**: Represents an order for a replacement appliance

## Technologies Used

- **Backend**: Django, Django REST Framework, PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Local development servers

## Future Improvements

- Add user authentication and authorization
- Implement real-time notifications for delivery updates
- Add more detailed appliance specifications
- Implement a more sophisticated matching algorithm for replacement options
- Add support for multiple appliance types