from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()
    print("Received:", data)
    return jsonify(
        {
            "status": "received",
            "message": "Review processed successfully",
            "receivedData": data,
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
