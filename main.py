from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime 
from flask_cors import CORS


dt = datetime.now()

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

class Profile(Resource):
    def get(self):
        return profile

    def post(self):
        profile["data"]["last_updated"] = dt.strftime("%c")
        profile["data"]["username"] = request.form['username']
        profile["data"]["role"] = request.form['role']
        profile["data"]["color"] = request.form['color']
        return profile

    def patch(self):
        profile["data"]["last_updated"] = dt.strftime("%c")

        data = (request.form)
        for key in data:
            profile["data"][key] = request.form[key]
        
        return profile


api.add_resource(Profile, "/profile")

if __name__ == "__main__":
    app.run(
        debug=True,
        #port = 3000,
        #host = "0.0.0.0"
    )
    