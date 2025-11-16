from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/text2embedding")
def hello():
    data = request.get_json()
    return {"data": data}


if __name__ == "__main__":
    app.run(debug=True)
