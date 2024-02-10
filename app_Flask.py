from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/double", methods=["POST"])
def double_number():
    data = request.json
    number = data["number"]
    return jsonify({"result": number * 2})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
