from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/operation/verify", methods=["GET"])
def verify_operation():
    print("Smooth running in progress")
    return jsonify({"status": "Running smoothly"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
