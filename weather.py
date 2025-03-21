import requests
import settings


def weather_by_city(city_name):
    weather_url = settings.Weather_URL
    params = {
        "key": settings.Weather_API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": "1",
        "lang": "ru",
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except (IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):   #Если нет интернета, если URL не верный(404) ошибка
        
        print("Сетевая ошибка")
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia"))
