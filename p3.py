import requests
from bs4 import BeautifulSoup

start = 0
result = []
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
for i in range(0, 10):
    html = requests.get('https://movie.douban.com/top250?start=' + str(start) + '&filter=', headers=header)

    html.encoding = 'utf-8'
    start += 25
    soup = BeautifulSoup(html.text, 'html.parser')

    for item in soup.find_all('div', 'info'):
        title = item.div.a.span.string

        yearline = item.find('div', 'bd').p.contents[2].string
        yearline = yearline.replace('\n', '')
        yearline = yearline.replace(' ', '')
        year = yearline[0:4]

        rating = item.find('span', {'class': 'rating_num'}).get_text()

        oneresult = [title, rating, year]
        result.append(oneresult)

print(result)