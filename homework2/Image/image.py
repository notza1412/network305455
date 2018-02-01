from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json
from werkzeug.datastructures import FileStorage

app = Flask (__name__)

api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('Picture', type=FileStorage, location='files')



class Test(Resource):
	def post(self):
		args = parser.parse_args()
		image = args['Picture']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"Upload success"}
		


api.add_resource(Test,'/image')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5001)
