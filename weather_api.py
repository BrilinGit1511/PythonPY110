import requests
from datetime import datetime

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    token = 'c8e6e851-5918-4009-a630-4c1e825eacfc'  # Вставить ваш токен
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    result = {
        'city': data['geo_object']['locality']['name'],
        'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
        'feels_like_temp': data['fact']['temp'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        'pressure': data['fact']['temp'],  # TODO Реализовать вычисление давления из данных полученных от API
        'humidity': data['fact']['temp'],  # TODO Реализовать вычисление влажности из данных полученных от API
        'wind_speed': data['fact']['temp'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        'wind_gust': data['fact']['temp'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
    }
    return result


if __name__ == "__main__":
    print(current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга
