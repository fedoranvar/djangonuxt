#!/usr/bin/env python
import os

# import names
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()
app = Flask("docs_app")
app.config["MONGODB_SETTINGS"] = [
    {
        "db": "docs",
        "host": "db",
        "port": 27017,
        "alias": "default",
    }
]
db.init_app(app)

@app.route("/")
def todo():
    # try:
    #     client.admin.command("ismaster")
    # except:
    #     return "Server not available"
    return "Hello from the MongoDB client!\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
