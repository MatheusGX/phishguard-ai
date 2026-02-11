from flask import Flask
from routes.scan import scan_blueprint

app = Flask(__name__)
app.register_blueprint(scan_blueprint)

@app.route('/')
def home():
    return "PhishGuard AI is running!"

if __name__ == '__main__':
    app.run(debug=True)