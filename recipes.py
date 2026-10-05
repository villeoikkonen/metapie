import db

def add_recipe(title, description, user_id, classes):
    sql = "INSERT INTO recipes (title, description, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, description, user_id])

    recipe_id = db.last_insert_id()

    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])
    return recipe_id

def add_vote(recipe_id, user_id, vote):
    sql = "INSERT INTO recipe_votes (recipe_id, user_id, vote) VALUES (?, ?, ?)"
    db.execute(sql, [recipe_id, user_id, vote])

def get_vote(recipe_id, user_id):
    sql = """SELECT vote
             FROM recipe_votes
             WHERE recipe_id = ? AND user_id = ?"""
    result = db.query(sql, [recipe_id, user_id])
    if not result:
        return None
    return result[0]["vote"]

def count_recipes():
    sql = "SELECT COUNT(*) AS total FROM recipes"
    result = db.query(sql)
    return result[0]["total"]

def get_user_votes(user_id):
    sql = "SELECT id, recipe_id, user_id, vote FROM recipe_votes WHERE user_id = ?"
    return db.query(sql, [user_id])

def get_recipe_votes(recipe_id):
    sql = "SELECT id, recipe_id, vote FROM recipe_votes WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def remove_vote(recipe_id, user_id):
    sql = "DELETE FROM recipe_votes WHERE recipe_id = ? AND user_id = ?"
    db.execute(sql, [recipe_id, user_id])

def get_recipes():
    sql = """SELECT recipes.id,
                    recipes.title,
                    users.id user_id,
                    users.username,
                    (SELECT COUNT(*)
                     FROM recipe_votes
                     WHERE recipe_votes.recipe_id = recipes.id
                       AND vote = 1) AS likes,
                    (SELECT COUNT(*)
                     FROM recipe_votes
                     WHERE recipe_votes.recipe_id = recipes.id
                       AND vote = -1) AS dislikes
             FROM recipes, users
             WHERE recipes.user_id = users.id
             ORDER BY recipes.id DESC"""
    return db.query(sql)

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)
    classes = {}
    for title, value in result:
        if title not in classes:
            classes[title] = []
        classes[title].append(value)
    return classes

def get_classes(recipe_id):
    sql = "SELECT title, value FROM recipe_classes WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def get_recipe(recipe_id):
    sql = """SELECT recipes.title,
                    recipes.id,
                    recipes.description,
                    users.username,
                    users.id user_id
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    result = db.query(sql, [recipe_id])
    return result[0] if result else None

def update_recipe(recipe_id, title, description, classes):
    sql = """UPDATE recipes SET title = ?,
                                description = ?
                            WHERE id = ?"""
    db.execute(sql, [title, description, recipe_id])

    sql = "DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])
    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

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