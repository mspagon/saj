from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Please Login!"


if __name__ == ("__main__"):
    application.run()
