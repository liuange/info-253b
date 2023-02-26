# liu_angela_lab-2.py
# 1. "add/<num1>/<num2>" - GET type - returns num1 + num2
# 2. "sub/<num1>/<num2>" - GET type - returns num1 - num2
# 3. "mul/<num1>/<num2>" - POST type - returns num1 * num2
# 4. "div/<num1>/<num2>" - POST type - returns num1/num2

from flask import Flask

app = Flask(__name__)
errorMessage = "Please use numbers only."

@app.route('/add/<num1>/<num2>', methods=["GET"])
def addition(num1, num2):
    try:
        return str(float(num1) + float(num2))
    except ValueError:
        return errorMessage

@app.route('/sub/<num1>/<num2>', methods=["GET"])
def subtraction(num1, num2):
    try:
        return str(float(num1) - float(num2))
    except ValueError:
        return errorMessage
    
@app.route('/mul/<num1>/<num2>', methods=["POST"])
def multiplication(num1, num2):
    try:
        return str(float(num1) * float(num2))
    except ValueError:
        return errorMessage

@app.route('/div/<num1>/<num2>', methods=["POST"])
def division(num1, num2):
    try:
        if float(num2) == 0:
            return "Cannot divide by zero."
        return str(float(num1) / float(num2))
    except ValueError:
        return errorMessage
    
