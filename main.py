from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return jsonify({"success": True, "msg":"Hello World" })
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name": "deez nuts",
        "email": "deeznuts@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get.json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)