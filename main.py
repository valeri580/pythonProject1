import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, data)

print(response.status_code)
if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

print (response.content)
response_json = response.json()
pprint.pprint(response_json)


