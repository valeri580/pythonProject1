api_key = "ваш ключ"

import requests as rq

city = "Moscow"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

response = rq.get(url)
print(response.status_code)
data = response.json()
print(data)

if response.status_code == 200:
    print(f"Погода в городе {city}")
    print(f"🌡️ Температура: {data['main']['temp']:.1f} °C")
    print(f"🔆 Погода: {data['weather'][0]['description']}")
    print(f"💧Влажность: {data['main']['humidity']} %")

