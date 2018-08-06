import datetime
from db.database_connection import db_connection, db
from db.query import fetch_all_recipes


def create_recipe_into_db(data):
    db.execute("INSERT INTO recipes (name, pre_time, difficulty, vegetarian, created_at) VALUES (%s, %s, %s, %s, %s)",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], datetime.datetime.now()))
    db_connection.commit()
    # db_connection.close()
    # db.close()

    message = {"message": "Recipe created"}
    status_code = 201
    return message, status_code


def update_recipe_into_db(data):
    db.execute("UPDATE recipes SET name=%s, pre_time=%s, difficulty=%s, vegetarian=%s, created_at=%s WHERE id=%s",
               (data['name'], data['pre_time'], data['difficulty'], data['vegetarian'], datetime.datetime.now(),
                data['id']))
    db_connection.commit()

    message = {"message": "Recipe Updated"}
    status_code = 200
    return message, status_code


def delete_recipe_from_db(data):
    recipes = fetch_all_recipes()
    for recipe in recipes:
        if recipe['id'] == int(data['id']):
            db.execute("DELETE FROM recipes where id=%s" % data['id'])
            db_connection.commit()
            message = {"message": "Recipe Deleted"}
            status_code = 200
            return message, status_code

    message = {"message": "Not found data"}
    status_code = 400
    return message, status_code
