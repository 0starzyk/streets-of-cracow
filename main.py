from bs4 import BeautifulSoup
import requests
import utils

if __name__ == '__main__':

    number_of_first_page = 1
    number_of_second_page = 365
    for i in range(number_of_first_page, 3):
        source = requests.get(f'https://www.kodypocztowe.info/krakow/page:{i}')
        soup = BeautifulSoup(source.content, 'html.parser')
        table = soup.find_all('tr', class_='_data')
        for row in table:
            text_row = filter(lambda x: '\n' not in x, map(lambda x: x.text, row))
            print(list(text_row))
