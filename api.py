from flask import Flask,request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'name':'test api'}
	def post(self):
		some_json = request.get_json()
		return {'you sent':some_json},201
class Multi(Resource):
	def get(self,num):
		return{'res':num*2}
class HelloName(Resource):
	def get(self,name,age):
		helloName = 'Hello '+name+' your age is '+str(age)
		return {'say':helloName}
api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(HelloName,'/hello/<name>&&<int:age>')
if __name__ == '__main__':
	app.run(host ='192.168.137.1',debug=True)