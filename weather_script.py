import requests

API_KEY = '6109ed07d9facafaf56b6884b079655b'  # Replace with your OpenWeatherMap API key
CITY = 'New York'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description']
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")

if __name__ == "__main__":
    fetch_weather()