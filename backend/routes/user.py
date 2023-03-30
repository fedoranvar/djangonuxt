from __main__ import app
from models.user import User


@app.route("/create")
def add_user():
    new_user = User(name=names.get_full_name())
    new_user.save()
    return str(new_user.id)


@app.route("/list")
def get_user():
    return User.objects.to_json()
