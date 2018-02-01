from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time
from datetime import datetime,date


app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('HBD')
	
def calculate_age(born):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))

class Date(Resource):
	def post(self):
		args = parser.parse_args()
		birthdate = args['HBD']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(calculate_age(datetime_object))
		return {"birthdate":birthdate,"age":age}

api.add_resource(Date,'/HBD')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5001)




