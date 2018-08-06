import datetime
from db.database_connection import db_connection, db


def create_recipe_into_db(data):
    db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], datetime.datetime.now()))
    db_connection.commit()
    # db_connection.close()
    # db.close()

    message = {"message": "Recipe created"}
    status_code = 201
    return message, status_code