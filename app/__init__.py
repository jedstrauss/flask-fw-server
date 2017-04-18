import sys
import os
from flask import Flask, request, render_template
from app.config import configure_app

app = Flask(__name__,
        instance_relative_config=True,
        template_folder='templates')

configure_app(app)

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server error: %s', (error))
    return render_template('500.html'),500

@app.errorhandler(Exception)
def unhandled_error(error):
    app.logger.error('Unhandled error: %s', (error))
    return render_template('500.html'),500

@app.route(app.config['BR_PATH'] + '/<path:filename>', methods=['PUT'])
def br_put(filename):
    with open(app.config['BR_FOLDER'] + filename, 'w+') as f:
        f.write(request.data)
    app.logger.info('File received: %s', (filename))
    return render_template('200.html'),200
