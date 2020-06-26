from flask import request
from helpers import databaseConnector as db

def user():
    db.SQLd.execute("SELECT user FROM tokens WHERE description = %s ORDER BY last_updated DESC LIMIT 1", (request.environ["HTTP_X_FORWARDED_FOR"].split(",")[0].strip(),))
    data = db.SQLd.fetchone()

    return data["user"]