from flask_restx import abort
from flask_sqlalchemy import BaseQuery, SQLAlchemy
import json
class CustomBaseQuery(BaseQuery):
    def get_or_error(self, ident):
        model_class_name = ''
        try:
            model_class_name = self._mapper_zero().class_.__name__
        except Exception as e:
            print(e) 

        instance = self.get(ident)
        if not instance:
            error_message = json.dumps({'status':'error','message': model_class_name })
            print('error_message',error_message)
            abort(404,status='error')
        return instance

db=SQLAlchemy(query_class=CustomBaseQuery)
