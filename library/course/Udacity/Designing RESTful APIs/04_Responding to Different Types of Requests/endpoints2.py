from flask import Flask, request 

app = Flask(__name__)

@app.route("/")
def mainPage():
	return "I made first(main) page"

@app.route("/puppies", methods=["GET", "POST"])
def puppiesFunction():
	if request.method == "GET":
		return get_puppies()

	elif request.method == "POST":
		return post_puppies()

@app.route("/puppies/<int:id>", methods=["GET", "PUT", "DELETE"])
def getPutDelete(id):
	if request.method == "GET":
		return get_id()

	elif request.method == "PUT":
		return get_put()

	elif request.method == "DELETE":
		return get_delete()

def get_delete():
	return "Method DELETE in /puppies/id"

def get_put():
	return "Method PUT in /puppies/id"

def get_id():
	return "Mehtod GET in /puppies/id"

def get_puppies():
	return "Method GET in '/puppies'"

def post_puppies():
	return "Method POST in '/puppies'"



if __name__ == "__main__":
	app.debug = True 
	app.run(host="localhost", port=8000)