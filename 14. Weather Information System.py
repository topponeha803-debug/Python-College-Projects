weather = {
    "korba": {
        "temperature": 32,
        "condition": "Sunny",
        "humidity": 55
    },

    "raipur": {
        "temperature": 34,
        "condition": "Cloudy",
        "humidity": 60
    },

    "delhi": {
        "temperature": 31,
        "condition": "Clear",
        "humidity": 50
    },

    "mumbai": {
        "temperature": 29,
        "condition": "Rainy",
        "humidity": 75
    },

    "indore": {
        "temperature": 30,
        "condition": "Partly Cloudy",
        "humidity": 58
    }
}


def show_weather():
    city = input("Enter city name: ").lower()

    if city not in weather:
        print("Weather data not available!")
        return

    data = weather[city]

    print("\n===== WEATHER REPORT =====")
    print("City:", city.title())
    print("Temperature:", data["temperature"], "°C")
    print("Condition:", data["condition"])
    print("Humidity:", data["humidity"], "%")


def show_cities():
    print("\nAvailable Cities:")

    for city in weather:
        print("-", city.title())


while True:
    print("\n===== WEATHER SYSTEM =====")
    print("1. Check Weather")
    print("2. Show Cities")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_weather()
    elif choice == "2":
        show_cities()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
