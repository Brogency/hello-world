from flask import Flask
import os

hostname = os.environ.get('HOSTNAME')
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    return "Flask inside {0} at {1}".format(hostname,path)


if __name__ == "__main__":
    app.run(debug=False,
            host='0.0.0.0')
