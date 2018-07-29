"""
This file only connect to DB
Created at: 28-07-2018
"""
__author__ = "Vubon Roy"

from psycopg2 import connect

from settings.settings import DATABASE

# Connect to an existing database
db_connection = connect(**DATABASE)

# Open a cursor to perform database operations
db = db_connection.cursor()

