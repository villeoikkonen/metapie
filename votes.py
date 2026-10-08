import db

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

def get_recipe_votes(recipe_id):
    sql = "SELECT id, recipe_id, vote FROM recipe_votes WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def get_user_votes(user_id):
    sql = "SELECT id, recipe_id, user_id, vote FROM recipe_votes WHERE user_id = ?"
    return db.query(sql, [user_id])

def remove_vote(recipe_id, user_id):
    sql = "DELETE FROM recipe_votes WHERE recipe_id = ? AND user_id = ?"
    db.execute(sql, [recipe_id, user_id])
    