from flask import Flask
from flask_restful import Api

from modules.api.v1.resources.Courts import Courts
from modules.api.v1.resources.Processes import Processes


app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Courts, '/api/v1/courts')
api.add_resource(Processes, '/api/v1/processes/<string:process_number>')

if __name__ == '__main__':
    app.run(debug=False, port='3333')
