# Weather_application in Django

This is a simple weather forecasting application built with Django. It allows users to check the current weather, temperature, and other weather-related information for different cities.

## Features

- Search weather by city na,e.
- Display temperature, humidity, wind speed, and weather conditions.
- Automatically fetch weather data from a third-party API.
- Display weather details in a user-friendly interface.

## Technologies Used

- Django: Web framework for building the app.
- OpenWeatherMap API: Used to fetch real-time weather data.
- HTML/CSS: For designing the front-end of the application.
- Bootstrap: For responsive design.

## Prerequisites

- Python 3.x
- Django 3.x or higher
- An OpenWeatherMap API key (free to sign up at [OpenWeatherMap](https://openweathermap.org/api))

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/shreya114/Weather_application.git
cd weather
```

### Step 2: Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install the dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure settings
1. In the weather/seetings.py file, set your OpenWeatherMap API key. Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
   WEATHER_API_KEY = 'YOUR_API_KEY'
2. Ensure that the database is set up correctly(if you're using one). For local development, SQLite is the default.

### Step 5: Run database migrations

```bash
python manage.py migrate
```

### Step 6: Start the development server

```bash
python manage.py runserver
```

## Usage

1. Navigate to the home page.
2. Enter the name of any city in the search bar.
3. View the weather details for the city you searched for, including temperature, humidity, wind speed, and weather condition.
