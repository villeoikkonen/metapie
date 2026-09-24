import db

def add_recipe(title, description, user_id, ingredients):
    sql = "INSERT INTO recipes (title, description, user_id, ingredients) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, user_id, ingredients])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.title,
                    recipes.id,
                    recipes.description,
                    recipes.ingredients,
                    users.username,
                    users.id user_id
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    result = db.query(sql, [recipe_id])
    return result[0] if result else None

def update_recipe(recipe_id, title, description, ingredients):
    sql = """UPDATE recipes SET title = ?,
                                description = ?
                            WHERE id = ?"""
    db.execute(sql, [title, description, recipe_id])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipe(query):
    sql = """SELECT id, title
             FROM recipes
             WHERE title LIKE ? OR description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])