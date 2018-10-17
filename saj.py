from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Add two numbers by entering using the add endpoint<BR><BR>Example:<BR>michaelspagon.com/add/55.15/22/"


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return "{} + {} = {}".format(num1, num2, num1 + num2)


if __name__ == ("__main__"):
    app.run()
