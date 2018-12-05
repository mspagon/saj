from flask import Flask
from flask import render_template

from models import models

import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == ("__main__"):
    models.initialize()
    app.run()
