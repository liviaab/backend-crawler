from flask_restful import Resource
import modules.main.controller as controller


class Courts(Resource):
    def get(self):
        return controller.get_courts()
