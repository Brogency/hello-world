from flask import Flask
import os

hostname = os.environ.get('HOSTNAME')
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside {0}".format(hostname)


if __name__ == "__main__":
    app.run(debug=False,
            host='0.0.0.0')
