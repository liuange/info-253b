# liu_angela_lab-4.py

from flask import Flask, request, Response, jsonify

app = Flask(__name__)
valueErrorMessage = "Please use numbers only."
typeErrorMessage = "Missing either num1 or num2 input."

@app.route('/add/<num1>/<num2>', methods=["GET"])
def addition(num1, num2):
    try:
        return  jsonify({"answer": float(num1) + float(num2)})
    except ValueError:
        return valueErrorMessage

@app.route('/sub', methods=["POST"])
def subtraction():
    try:
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        return jsonify({"answer": float(num1) - float(num2)})
    except TypeError:
        return typeErrorMessage
    except ValueError:
        return valueErrorMessage
    
@app.route('/mul', methods=["POST"])
def multiplication():
    try:
        num1 = request.get_json().get("num1")
        num2 = request.get_json().get("num2")
        return jsonify({"answer": float(num1) * float(num2)})
    except TypeError:
        return typeErrorMessage
    except ValueError:
        return valueErrorMessage

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)