from flask import Flask, send_from_directory
from routes.scan import scan_blueprint
import os

app = Flask(__name__)
app.register_blueprint(scan_blueprint)

@app.route('/')
def home():
    return send_from_directory("../frontend/templates", "index.html")

if __name__ == '__main__':
    app.run(debug=True)