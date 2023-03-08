from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    source = requests.get('https://www.kodypocztowe.info/krakow/page:1')
    soup = BeautifulSoup(source.content, 'html.parser')
    table = soup.find_all('tr', class_='_data')
    for row in table:
        text_row = filter(lambda x: '\n' not in x, map(lambda x: x.text, row))
        print(list(text_row))
