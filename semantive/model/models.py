from flask import g
import shelve


def get_db():
    if 'db' not in g:
        g.db = shelve.open('data.db')

    return g.db


@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
