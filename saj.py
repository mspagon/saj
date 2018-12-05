from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/drumset/')
def drumset():
    return app.send_static_file('drumset/index.html')


if __name__ == ("__main__"):
    app.run()
