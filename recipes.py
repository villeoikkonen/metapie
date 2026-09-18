import db

def add_recipe(title, description, user_id):
    sql = "INSERT INTO recipes (title, description, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, description, user_id])