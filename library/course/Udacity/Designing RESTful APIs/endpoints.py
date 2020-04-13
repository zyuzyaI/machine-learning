from flask import Flask 

app = Flask(__name__)

@app.route("/")
def helloPage():
	return "Hello my page!"

@app.route("/puppies")
def puppiesFunction():
	return "Yes, puppies!"

@app.route("/puppies/<int:id>")
def pageId(id):
	return "This method will act on the puppy with id %s" % id

if __name__ == "__main__":
	app.debug = True 
	app.run(host="localhost", port=8000)