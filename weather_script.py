# Fetch weather data from OpenWeatherMap API

import requests

def get_weather(city, api_key):
    """
    Fetches weather data for a given city from OpenWeatherMap API.
    Returns temperature, humidity, and weather description.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error: Unable to fetch weather data!"
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    return f"Temperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description}"

# Example usage:
# Replace 'your_api_key' with your actual OpenWeatherMap API key
# city = input("Enter city name: ")
# api_key = 'your_api_key'
# print(get_weather(city, api_key))