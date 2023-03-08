from bs4 import BeautifulSoup
import requests
import psycopg2
from psycopg2 import OperationalError
from time import time

import utils
from utils import *
import config

if __name__ == '__main__':
    password = input('Password: ')
    try:
        connection = psycopg2.connect(get_connection_string(password))
        print('Database connected successfully')
        start = time()

        for index in range(config.number_of_first_page, config.number_of_last_page):
            source = requests.get(config.url + str(index))
            soup = BeautifulSoup(source.content, 'html.parser')
            table = soup.find_all('tr', class_='_data')
            for row in table:
                text_row = list(filter(lambda x: '\n' not in x, map(lambda x: x.text, row)))
                postal_code = text_row[0]
                district = text_row[2]
                street = text_row[3]
                numbers = text_row[4]
                utils.add_street(connection, postal_code, district, street, numbers)

        stop = time()
        print(f'Execution time: {stop - start}')
        connection.close()
    except OperationalError:
        print('Error')
