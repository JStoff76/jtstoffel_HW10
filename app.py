# BAIS:3300 — Digital Product Management
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Step 1: return text (Hello World!!) for first screenshot
    return "Hello World!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
