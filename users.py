import db
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])


def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None
    user = result[0]
    if not check_password_hash(user["password_hash"], password):
        return None
    return user["id"]