import requests


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=55.7512&longitude=37.6184&current_weather=true"
    response = None
    data = None
    temp = None
    wind = None

    response = requests.get(url)
    data = response.json()
    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]

    print("Текущая погода в Москве:")
    print(f"Температура: {temp}°C")
    print(f"Скорость ветра: {wind} км/ч")


if __name__ == "__main__":
    get_weather()