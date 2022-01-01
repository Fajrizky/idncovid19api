# import Libraries
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Init objects flask
app = Flask(__name__)

# Init objects flask_restful
api = Api(app)

# Init objects flask_cors
CORS(app)

# init empty variable type dictionary to store data
identity = {}  # dictionary == json

# class to handle request


class ContohResouce(Resource):
    # Define method get and post
    def get(self):
        reponse = {'message': 'Hello World'}
        return identity

    def post(self):
        name = request.form["name"]
        age = request.form["age"]
        identity["name"] = name
        identity["age"] = age
        response = {'message': 'Data has been successfully added'}
        return response


# Setup resource
api.add_resource(ContohResouce, '/api', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, port=5005)
