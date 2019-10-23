from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from modules.api.v1.resources.Courts import Courts
from modules.api.v1.resources.Processes import Processes


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Routes
api.add_resource(Courts, '/api/v1/courts')
api.add_resource(Processes, '/api/v1/processes/<string:process_number>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='3333')
