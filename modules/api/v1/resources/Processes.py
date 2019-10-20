from flask_restful import Resource
import modules.main.controller as controller


class Processes(Resource):
    def get(self, process_number):
        return controller.get_process_info(process_number)
