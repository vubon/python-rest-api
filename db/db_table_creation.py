from db.database_connection import db_connection, db

table = "CREATE TABLE newtable (foo INTEGER, bar TEXT);"

recipe_table = "CREATE TABLE recipes (id serial PRIMARY KEY , name VARCHAR(100), " \
               "pre_time INTEGER CHECK ( pre_time > 0), difficulty INTEGER check ( difficulty > 0)," \
               " vegetarian BOOLEAN, created_at TIMESTAMP )"

# db.execute("CREATE TABLE vubon (id serial PRIMARY KEY, num integer, data varchar);")

recipe_rating = "CREATE TABLE recipe_rating (recipe_id INTEGER REFERENCES recipes, rated INTEGER CHECK( rated > 0))"

db.execute(recipe_table)
db.execute(recipe_rating)

db_connection.commit()
db_connection.close()
db.close()
