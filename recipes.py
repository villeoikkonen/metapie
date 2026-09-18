import db

def add_recipe(title, description, user_id, ingredients):
    sql = "INSERT INTO recipes (title, description, user_id, ingredients) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, user_id, ingredients])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.title,
                    recipes.description,
                    recipes.ingredients,
                    users.username
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    return db.query(sql, [recipe_id])[0]