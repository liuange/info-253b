from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

serverMap = "serverMapping.json"

@app.route("/message", methods=["POST"])
def receiveMessage():
    input = request.get_json()
    # receives data as {'data': {'command': None, 'message': 'ms'}}
    data = input["data"]["message"]
    if data[0] == "/":
        parsed = data.split(" ", 1)
        command = parsed[0]
        command = command[1:]
        if len(parsed) < 2:
            msg = ""
        else:
            msg = parsed[1]
    else: 
        command = None
        msg = "No command on this one!"
    # create data to pass
    data = {"data": {"command": command, "message": msg}}
    # check if command is a key in the JSON file 
    with open(serverMap, "r+") as f:
        servers = json.load(f)
    if command in servers.keys():
        server_url = servers[command]
        r = requests.post(server_url + "/execute", json=data)
        return r.content
    return data

@app.route("/register", methods=["POST"])
def registerCommand():
    '''The “/register” endpoint allows storage Server URL for a particular command, i.e.
    input: {"data": { "command": [name of command], "server_url": [url of server that executes command] }}    
    output: {"data": { "command" [name of command], "message": "saved"}}
    '''
    input = request.get_json()
    command = input["data"]["command"]
    server_url = input["data"]["server_url"]
    with open(serverMap, "r+") as f:
        servers = json.load(f)
        servers.update({command: server_url})
        f.seek(0) # resets position
        json.dump(servers, f)
    output = {"data": { "command": command, "message": "saved"}}
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)