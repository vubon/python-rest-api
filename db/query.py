import json
from db.database_connection import db


def fetch_all_recipes():
    # db.execute(
    #     "SELECT recipes.id, name, pre_time, difficulty, vegetarian, created_at, ROUND(AVG(rated),2) FROM recipes INNER JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id")

    db.execute(
        "SELECT recipes.id, name, pre_time, difficulty, vegetarian, created_at, ROUND(AVG(rated),2) "
        "FROM recipes LEFT JOIN recipe_rating ON recipe_id=id GROUP BY recipes.id ORDER BY id ASC")

    recipes = []
    for item in db.fetchall():
        data = dict()
        data['id'] = item[0]
        data['name'] = item[1]
        data['pre_time'] = item[2]
        data['difficulty'] = item[3]
        data['vegetarian'] = item[4]
        data['created_at'] = item[5].strftime('%Y-%m-%dT%H:%M:%S')
        data['average_rating'] = str(item[6])
        recipes.append(data)
    # serializer = json.dumps(db.fetchall(), indent=4, sort_keys=True, default=str)
    return recipes
