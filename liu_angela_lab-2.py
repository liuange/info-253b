from flask import Flask

app = Flask(__name__)

@app.route('/add/<num1>/<num2>', methods=["GET"])
def addition(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Please use integers only."
    return str(num1 + num2)

@app.route('/sub/<num1>/<num2>', methods=["GET"])
def subtraction(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Please use integers only."
    num1 = int(num1)
    num2 = int(num2)
    return str(num1 - num2)

@app.route('/mul/<num1>/<num2>', methods=["POST"])
def multiplication(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Please use integers only."
    num1 = int(num1)
    num2 = int(num2) 
    return str(num1 * num2)

@app.route('/div/<num1>/<num2>', methods=["POST"])
def division(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Please use integers only."
    if num2 == 0:
        return "Cannot divide by zero."
    return str(num1 / num2)

    
# 1. "add/<num1>/<num2>" - GET type - returns num1 + num2
# 2. "sub/<num1>/<num2>" - GET type - returns num1 - num2
# 3. "mul/<num1>/<num2>" - POST type - returns num1 * num2
# 4. "div/<num1>/<num2>" - POST type - returns num1/num2

# EXAMPLE
# from flask import Flask
# import json

# app = Flask(__name__)

# quote_db = {
#   'sunday': "Life is about making an impact, not making an income. \
#   –Kevin Kruse",
#   'monday': "Whatever the mind of man can conceive and believe, it can achieve. \
#   –Napoleon Hill",
#   'tuesday': "Strive not to be a success, but rather to be of value. \
#   –Albert Einstein",
#   'wednesday': "You miss 100% of the shots you don’t take. \
#   –Wayne Gretzky",
#   'thursday': "Every strike brings me closer to the next home run. \
#   –Babe Ruth",
#   'friday': "We become what we think about. \
#   –Earl Nightingale",
#   'saturday': "Life is what happens to you while you’re busy making other plans. \
#   –John Lennon",
# }

# @app.route('/quote/<day_of_week>')
# def quote_of_the_day(day_of_week):
#   response = {"day": day_of_week, "quote": quote_db[day_of_week.lower()]}

#   return json.dumps(response)

