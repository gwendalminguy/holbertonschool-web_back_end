"""
app.py
Minimal Flask Application
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
async def root():
    return jsonify({"message": "Bienvenue"}, status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
