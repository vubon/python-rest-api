import json
from db.database_connection import db


def fetch_all_recipes():
    db.execute("SELECT * FROM recipes;")
    recipes = []
    for item in db.fetchall():
        data = dict()
        data['id'] = item[0]
        data['name'] = item[1]
        data['pre_time'] = item[2]
        data['difficulty'] = item[3]
        data['vegetarian'] = item[4]
        data['created_at'] = item[5].strftime('%Y-%m-%dT%H:%M:%S')
        recipes.append(data)
    # serializer = json.dumps(db.fetchall(), indent=4, sort_keys=True, default=str)
    print(recipes)
    return recipes
