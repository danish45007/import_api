try:
    from flask import Flask
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask_limiter.util import get_remote_address
    from flask_limiter import Limiter
    from flasgger import Swagger
    from flasgger.utils import swag_from
    from flask_restful_swagger import swagger
    

except Exception as e:
    print("some modules are missing {}".format(e))



app = Flask(__name__)
api = Api(app)

limiter = Limiter(app,key_func=get_remote_address)
limiter.init_app(app)

api = swagger.docs(Api(app),apiVersion = '1',api_spec_url= "/docs")


parser = reqparse.RequestParser()
parser.add_argument('zip',type=str,required=True,help="Please add zip code")
parser.add_argument('city',type=str,required=True,help="Please enter city")


class Myapi(Resource):
    def __init__(self):
        self.__zip_code = parser.parse_args().get('zip',None)
        self.__city = parser.parse_args().get('city',None)


    def get(self):
        if (len(self.__city)>2) and (len(self.__zip_code)>2):
            return {"response":200,
            "data":parser.parse_args()
            }
        else:
            return {"response":400}


    
    
    #cont...


api.add_resource(Myapi,'/weather/')

if __name__ == "__main__":
    app.run(debug=True)


    