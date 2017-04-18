import sys
import os
from flask import Flask, request
from app.config import configure_app

app = Flask(__name__,instance_relative_config=True)
configure_app(app)

@app.route(app.config['BR_PATH'] + '/<path:filename>', methods=['PUT'])
def br_put(filename):
    try:
        with open(app.config['BR_FOLDER'] + filename, 'w+') as f:
            f.write(request.data)
    except:
        e = sys.exc_info()
        return "Internal Server Error\n",500
    else:
        return "OK\n",200
