import db

def add_ingredient(recipe_id, name, amount, unit):
    sql = "INSERT INTO ingredients (recipe_id, name, amount, unit) VALUES (?, ?, ?, ?)"
    db.execute(sql, [recipe_id, name, amount, unit])

def get_ingredients(recipe_id):
    sql = "SELECT id, name, amount, unit FROM ingredients WHERE recipe_id = ? ORDER BY id"
    return db.query(sql, [recipe_id])

def get_ingredient(ingredient_id):
    sql = """SELECT id, name, amount, unit, recipe_id
             FROM ingredients
             WHERE id = ?"""

    result = db.query(sql, [ingredient_id])
    return result[0] if result else None

def update_ingredient(ingredient_id, name, amount, unit):
    sql = """UPDATE ingredients SET name = ?,
                                    amount = ?,
                                    unit = ?
                            WHERE id = ?"""
    db.execute(sql, [name, amount, unit, ingredient_id])

def remove_ingredient(ingredient_id):
    sql = "DELETE FROM ingredients WHERE id = ?"
    db.execute(sql, [ingredient_id])

'''
def find_ingredient(query):
    sql = """SELECT id, title
             FROM recipes
             WHERE title LIKE ? OR description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
'''