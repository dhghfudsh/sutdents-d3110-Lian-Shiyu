import requests

url = "https://www.film.ru/"
response = requests.get(url)

print(response.text)
print(response.encoding)
response.encoding = 'utf-8'

print(response.text)
