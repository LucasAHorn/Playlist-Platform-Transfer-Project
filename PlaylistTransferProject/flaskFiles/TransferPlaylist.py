from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is currently in the process of testing, will be updated with good code soon
@app.route('/api/YoutubeToSpotify', methods=['POST', 'GET'])
def YoutubeToSpotify():
    functionSuccess = 0 # False
    data = request.get_json()
    name = data.get('name')
    if name == "Lucas":
        functionSuccess = 1
    data = {"functionSuccess": functionSuccess}
    return jsonify(data)


app.run(host="0.0.0.0", port="5000")    # This should be fine