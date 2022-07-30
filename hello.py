from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

names={
    "Tim":{"age":19,"sex":"male"},
    "Rachel":{"age":19,"sex":"female"}
}
class HelloWorld(Resource):
    def get(self,name):
        return names[name]
    
api.add_resource(HelloWorld,"/helloworld/<name>")
if __name__=="__main__":
    app.run(debug=True)
 
