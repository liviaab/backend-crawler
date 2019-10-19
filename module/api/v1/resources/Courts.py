from flask_restful import Resource

class Courts(Resource):
    def get(self):
        return {'teste': [{'nome': 'Lívia Almeida Barbosa'}, {'nome': 'Joaquim'}] }
