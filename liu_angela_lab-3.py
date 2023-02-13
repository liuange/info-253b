from flask import Flask, request, Response, jsonify
import json 

app = Flask(__name__)
filename = "quotes.json"

# helper function to get data from quotes JSON
def loadDataFromFile():
    with open(filename) as f:
        data = json.load(f)
    return data

# helper function to check JSON inputs are valid
def validateData(key = None):
    data = loadDataFromFile()
    jsonKeys = data.keys()
    validDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # handle key checks
    if key != None:
        key = key.lower()
        # ALL: is the key a valid day?
        if key not in validDays:
            return data, 400
        # GET: is provided key in the json?
        elif key not in list(jsonKeys):
            return data, 204
        else:
            return data, 200
    # is json empty?
    elif len(jsonKeys) == 0: 
        return data, 204
    else:
        return data, 200

# Route for Root (prompt 1) - Returns json, 200 code
@app.route("/", methods=["GET"])
def index():
    data, responseCode = validateData()
    return jsonify(data), responseCode

# Route by Day
@app.route("/<day>", methods=["GET"])
def getByDay(day):
    data, responseCode = validateData(day)
    if responseCode == 200:
        return jsonify({day: data[day]}), responseCode
    else:
        return {}, responseCode

# Add a quote from request body
@app.route("/", methods=["POST"])
def addDayAndQuote():
    # get day key from request body
    day = request.get_json().get("day")
    data, responseCode = validateData(day)
    # if day key is not in json (204)
    if responseCode == 204: 
        # get quote add to JSON 
        quote = request.get_json().get("quote")
        data[day] = quote
        with open(filename, "w") as f:
            json.dump(data, f)
        return jsonify({day: data[day]}), 201
    elif responseCode == 200:
        # this means key exists already
        return {}, 400
    else: 
        return {}, responseCode


# Delete a quote using URL param
@app.route("/<day>", methods=["DELETE"])
def deleteQuote(day):
    # get day key from request body
    data, responseCode = validateData(day)
    # print(responseCode)
    # If it does exist, remove it from your JSON and then return a 200 back with an empty body. 
    if responseCode == 200: 
        data.pop(day)
        with open(filename, "w") as f:
            json.dump(data, f)
        return {}, responseCode
    # If it doesn’t, return a 404 error message with an empty body.    
    else: 
        return {}, 404
    
# Update a quote using a day URL param, new quote in body
@app.route("/<day>", methods=["PUT"])
def updateQuote(day):
    # Your task is to check if that day exists in your json and update it with the value of “quote” from the Request Body.
    quote = request.get_json().get("quote")
    data, responseCode = validateData(day)
    print(responseCode)
    # If it does exist, update it in your JSON and then return a 200 back with the following response. 
    if responseCode == 200: 
        data[day] = "updated " + quote
        with open(filename, "w") as f:
                json.dump(data, f)
        return jsonify({day: data[day]}), 200
    # If it doesn’t exist, create a new entry for that day and return a 201 with the same response body as you use for POST call:
    elif responseCode == 204:
        data[day] = quote
        with open(filename, "w") as f:
                json.dump(data, f)
        return jsonify({day: data[day]}), 201
    else:
        return {}, responseCode
# python -m flask --app liu_angela_lab-2 run --host=0.0.0.0 --port=5050