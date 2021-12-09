from flask import Flask
from flask_restx import Api,Resource
from config import DevConfig
from models import Dsm,User,Store,Sku,Role
from exts import db
from flask_sqlalchemy import SQLAlchemy

 
app=Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

api=Api(app,doc='/docs')


@api.route('/login',methods=['GET'])
class Login(Resource):
    def get(self):
        return {'status': 'success'}

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "Dsm":Dsm,
        "User":User,
        "Store":Store,
        "Sku":Sku,
        "Role":Role,
    }

if __name__ == '__main__':
    app.run()