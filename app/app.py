from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app, title='Calculadora', version='1.0', doc='/swagger')

operator_ns = api.namespace('/')

@operator_ns.route('/soma')
@operator_ns.doc(description='Soma')
class Soma(Resource):
    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a + b}

@operator_ns.route('/multiplicacao')
@operator_ns.doc(description='Multiplicação')
class Multiplicacao(Resource):
    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a * b}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)


