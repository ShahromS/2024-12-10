from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask App!</h1><p>Hello, World!</p>"

@app.route("/time")
def current_time():
    now = datetime.now()
    return jsonify({"current_time": now.strftime("%Y-%m-%d %H:%M:%S")})



if __name__ == "__main__":
    app.run(debug=True)
