from flask_restful import Resource

class Processes(Resource):
    def get(self, process_number):
        return {'teste': { 'nome': 'Lívia Almeida Barbosa', 'process_number': process_number }}
