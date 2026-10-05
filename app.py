import secrets
import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
import db
import config
import recipes
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def index():
    user_count = users.count_users()
    recipe_count = recipes.count_recipes()
    return render_template("index.html", 
                           user_count=user_count, recipe_count=recipe_count
                           )

# Show all recipes page
@app.route("/recipes")
def show_recipes():
    all_recipes = recipes.get_recipes()
    return render_template("recipes.html", recipes=all_recipes)

# Show recipe page
@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    classes = recipes.get_classes(recipe_id)
    user_vote = None
    recipe_votes = recipes.get_recipe_votes(recipe_id)
    if "user_id" in session:
        user_vote = recipes.get_vote(recipe_id, session["user_id"])
    return render_template("show_recipe.html", 
                           recipe=recipe, classes=classes, user_vote=user_vote, recipe_votes=recipe_votes)

# User registeration
@app.route("/register")
def register():
    return render_template("register.html")

# Show user page
@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    user_recipes = users.get_items(user_id)
    user_votes = recipes.get_user_votes(user_id)
    return render_template("show_user.html", user=user, recipes=user_recipes, votes=user_votes)

# Create new user
@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        error_msg = "VIRHE: salasanat eivät ole samat"
        return render_template("/register.html", error_msg=error_msg)
    if not password1.strip():
        error_msg = "VIRHE: epäkelpo salasana, salasana ei saa olla tyhjä tai sisältää pelkkiä välilyöntejä."
        return render_template("/register.html", error_msg=error_msg)
    elif len(password1) < 5:
        error_msg = "VIRHE: epäkelpo salasana, salasanan on oltava vähintään 5 merkkiä pitkä."
        return render_template("/register.html", error_msg=error_msg)

    try:
        if not username.strip():
            error_msg = "VIRHE: epäkelpo käyttäjänimi, käyttäjänimi ei saa olla tyhjä tai sisältää pelkkiä välilyöntejä."
            return render_template("/register.html", error_msg=error_msg)
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        error_msg = "VIRHE: tunnus on jo varattu"
        return render_template("/register.html", error_msg=error_msg)

    return redirect("/")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)

        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            error_msg = "VIRHE: väärä tunnus tai salasana"
            return render_template("/login.html", error_msg=error_msg)

# Logout
@app.route("/logout")
def logout():
    require_login()
    del session["username"]
    del session["user_id"]
    return redirect("/")

# Find recipe
@app.route("/find_recipe")
def find_recipe():
    query = request.args.get("query")
    if query:
        results = recipes.find_recipe(query)
    else:
        query = ""
        results = []
    return render_template("find_recipe.html", query=query, results=results)

# Add new recipe
@app.route("/new_recipe")
def new_recipe():
    require_login()
    classes = recipes.get_all_classes()
    return render_template("new_recipe.html", classes=classes)

# Edit existing recipe
@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    require_login()
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    all_classes = recipes.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in recipes.get_classes(recipe_id):
        classes[entry["title"]] = entry["value"]

    return render_template("edit_recipe.html", recipe=recipe, all_classes=all_classes, classes=classes)

# Update recipe
@app.route("/update_recipe", methods=["POST"])
def update_recipe():
    require_login()
    check_csrf()
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)

    classes = []
    all_classes = recipes.get_all_classes()
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    recipes.update_recipe(recipe_id, title, description, classes)
    return redirect("/recipe/" + str(recipe_id))

# Remove recipe
@app.route("/remove_recipe/<int:recipe_id>", methods=["GET", "POST"])
def remove_recipe(recipe_id):
    require_login()
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    if request.method == "GET":
        return render_template("remove_recipe.html", recipe=recipe)
    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            recipes.remove_recipe(recipe_id)
            return redirect("/")
        else:
            return redirect("/recipe/" + str(recipe_id))

# Create a new recipe
@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    require_login()
    check_csrf()
    title = request.form["title"]
    if not title.strip() or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)
    user_id = session["user_id"]

    all_classes = recipes.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    recipe_id = recipes.add_recipe(title, description, user_id, classes)
    if recipe_id == None:
        recipe_id = db.last_insert_id()

    return redirect("/recipe/" + str(recipe_id))

# Vote recipe
@app.route("/vote_recipe", methods=["POST"])
def vote_recipe():
    require_login()
    check_csrf()
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(403)

    vote = request.form["vote"]
    if vote not in ["1", "-1"]:
        if vote == "0":
            recipes.remove_vote(recipe_id, session["user_id"])
            return redirect("/recipe/" + str(recipe_id))
        else:
            abort(400)

    recipes.add_vote(recipe_id, session["user_id"], int(vote))

    return redirect("/recipe/" + str(recipe_id))