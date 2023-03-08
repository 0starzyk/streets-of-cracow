from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    source = requests.get('https://www.kodypocztowe.info/krakow')
    soup = BeautifulSoup(source.content, 'html.parser')
    print(soup.prettify())
