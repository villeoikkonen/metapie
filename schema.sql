CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE recipe_classes (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes ON DELETE CASCADE,
    title TEXT,
    value TEXT
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    amount TEXT,
    unit TEXT,
    recipe_id INTEGER REFERENCES recipes ON DELETE CASCADE
);

CREATE TABLE recipe_votes (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    vote INTEGER CHECK (vote IN (-1, 1)),
    UNIQUE (recipe_id, user_id)
);

CREATE INDEX idx_votes_recipe_vote
ON recipe_votes (recipe_id, vote);
