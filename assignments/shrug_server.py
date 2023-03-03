from flask import Flask, jsonify, request

app = Flask(__name__)

# receives {"data": {"command": "shrug", "message": [message that was sent] }}
@app.route("/execute", methods=["POST"])
def executeMessage():
    input = request.get_json()
    if input["data"]["command"] == "shrug":
        data = input["data"]["message"]
        output = jsonify({"data": {"command": "shrug", "message": data + "¯\_(ツ)_/¯"}})
        return output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5051)