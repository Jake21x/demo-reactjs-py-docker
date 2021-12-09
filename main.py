from flask import Flask
from flask_restx import Api,Resource
from config import DevConfig

app=Flask(__name__)

app.config.from_object(DevConfig)

api=Api(app,doc='/docs')


@api.route('/login',methods=['GET'])
class Login(Resource):
    def get(self):
        return {'status': 'success'}


if __name__ == '__main__':
    app.route()