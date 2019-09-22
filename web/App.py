# Template from Flask Restful website
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
from flask import Flask
from flask_restful import Resource, Api
#from resources.Greeting import Greeting

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
print("Hello")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)