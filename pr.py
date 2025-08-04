import requests

urls = [
    "https://divan.ru/category/divany?page={}",
    "http://www.divan.ru/category/divany?page={}",
    "http://divan.ru/category/divany?page={}",
    "https://www.divan.ru/category/divany?page={}"
]

for url in urls:
    print(f"Проверка: {url}")
    try:
        session = requests.Session()
        seen = set()
        resp = session.get(url, allow_redirects=False, timeout=10)
        chain = []
        while resp.is_redirect or resp.is_permanent_redirect:
            location = resp.headers.get('Location')
            chain.append((resp.status_code, resp.url, location))
            # Проверяем на зацикливание
            if location in seen:
                print(f"  Обнаружен цикл редиректа на {location}!")
                break
            seen.add(location)
            # Формируем абсолютный URL
            resp = session.get(location, allow_redirects=False, timeout=10)
        else:
            # Если редиректы закончились, выводим конечный статус
            chain.append((resp.status_code, resp.url, None))

        for i, (status, from_url, to_url) in enumerate(chain):
            if to_url:
                print(f"  [{i+1}] {status} {from_url} -> {to_url}")
            else:
                print(f"  [{i+1}] {status} Конечный адрес: {from_url}")

        print('-' * 40)
    except Exception as e:
        print(f"  Ошибка: {e}")
        print('-' * 40)