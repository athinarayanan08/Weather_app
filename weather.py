
def get_weather(city_name):
    mock_data = {
        "London": {
            "country": "GB",
            "temp": 15,
            "description": "light rain",
            "humidity": 82,
            "wind_speed": 4.1
        },
        "New York": {
            "country": "US",
            "temp": 22,
            "description": "clear sky",
            "humidity": 60,
            "wind_speed": 2.5
        },
        "InvalidCity": None
    }

    data = mock_data.get(city_name)
    if data:
        print(f"\nWeather in {city_name}, {data['country']}:")
        print(f"Temperature: {data['temp']}°C")
        print(f"Weather: {data['description']}")
        print(f"Humidity: {data['humidity']}%")
        print(f"Wind Speed: {data['wind_speed']} m/s")
    else:
        print("\nCity not found or data unavailable.")

if __name__ == "__main__":
    # Simulated test cases
    test_cases = [
        "London",
        "New York",
        "InvalidCity"
    ]

    for city in test_cases:
        print(f"\nFetching weather for: {city}")
        get_weather(city)
