from flask import Flask
from flask import request
import pprint

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    content = request.get_json(silent=True)

    pprint.pprint(content)
    return content
