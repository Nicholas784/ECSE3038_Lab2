from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime 
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 
api = Api(app)

@app.route("/")
def welcome():
    return "Welcome!"

profile = {
    "success": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51 PM", 
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }
}

tank_info = []
tank_id = 0

class Profile(Resource):
    def get(self):
        return profile

    def post(self):
        profile["data"]["last_updated"] = datetime.now().strftime("%c")
        profile["data"]["username"] = request.form['username']
        profile["data"]["role"] = request.form['role']
        profile["data"]["color"] = request.form['color']
        return profile

    def patch(self):
        profile["data"]["last_updated"] = datetime.now().strftime("%c")

        data = (request.form)
        for key in data:
            profile["data"][key] = request.form[key]
        
        return profile

class Data(Resource):
    def get(self):
        return jsonify(tank_info)


    def post(self):
        global tank_id
        tank_id += 1
        tank = {}

        tank["id"] = tank_id
        tank["location"] = request.form['location']
        tank["lat"] = request.form['lat']
        tank["long"] = request.form['long']
        tank["percentage_full"] = request.form['percentage_full']

        tank_info.append(tank)
        return jsonify(tank_info)


class Data2(Resource):
    def patch(self, tank_id):
        for item in tank_info: 
            if item["id"] == tank_id:
                data = (request.form)
                for key in data:
                    item[key] = request.form[key]

        return jsonify(tank_info)

    def delete(self, tank_id):
        for item in tank_info:
            if item["id"] == tank_id:
                tank_info.remove(item)

        return {"success": True}


api.add_resource(Profile, "/profile")
api.add_resource(Data, "/data")
api.add_resource(Data2, "/data/<int:tank_id>")

if __name__ == "__main__":
    app.run(
        debug=True,
        port = 3000,
        host = "0.0.0.0"
    )
    