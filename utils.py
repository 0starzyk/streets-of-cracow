import config


def create_street_table_query():
    return '''CREATE TABLE streets (
id SERIAL PRIMARY KEY,
postal_code VARCHAR NOT NULL,
district  VARCHAR NOT NULL,
street VARCHAR NOT NULL,
numbers VARCHAR
);'''


def get_connection_string(password):
    return config.connection_string.replace('***', password)


def add_street():
    pass