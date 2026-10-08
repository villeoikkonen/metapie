import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM recipe_votes")
db.execute("DELETE FROM recipe_classes")
db.execute("DELETE FROM recipes")
db.execute("DELETE FROM users")

user_count = 1000
recipe_count = 10**6
votes_per_recipe = 10

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (id, username) VALUES (?, ?)",
               [i, "user" + str(i)])

for recipe_id in range(1, recipe_count + 1):
    db.execute(
        """INSERT INTO recipes (id, title, description, user_id)
           VALUES (?, ?, ?, ?)""",
        [
            recipe_id,
            f"Resepti {recipe_id}",
            "Sekoita ainekset ja kypsennä.",
            random.randint(1, user_count)
        ]
    )

    voters = random.sample(range(1, user_count + 1), votes_per_recipe)

    for user_id in voters:
        db.execute(
            """INSERT INTO recipe_votes (recipe_id, user_id, vote)
               VALUES (?, ?, ?)""",
            [recipe_id, user_id, random.choice([-1, 1])]
        )

db.commit()
db.close()
