import requests


url = 'https://fake-json-api.mock.beeceptor.com/users'


response = requests.get(url)


if response.status_code == 200:

    print(response.json())
else:
    print(f'Ошибка при запросе: {response.status_code}')