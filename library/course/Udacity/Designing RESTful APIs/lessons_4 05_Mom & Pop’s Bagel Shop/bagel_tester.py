# from urllib import urlencode
from httplib2 import Http
import base64
import json
import sys

print("Running Endpoint Tester...")
address = input("Please enter the address of the server you want access,\n\
	If left blank the connection will be setto 'http://localhost:8000'")
if address == "":
	address = "http://localhost:8000"

# TEST ONE -- TRY TO MAKE A NEW USER
try:
	url = address + "/users"
	h = Http()
	data =  dict(username = "DimaKyn", 
				password="Udacity")
	resp, result = h.request(url, 
							"POST", 
							body=json.dumps(data), 
							headers={"Content-Type": "application/json"})
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])
except Exception as err:
	print("Test 1 FAILED: Could not make a new user")
	print(err.args)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully made a new user")
print("-----------------------------------------------")

# TEST TWO -- ADD NEW BAGELS TO THE DATABASE
try: 
	h = Http()
	h.add_credentials('DimaKyn','Udacity')
	url = address + "/bagels"
	data =  dict(username = "DimaKyn", 
				password = "Udacity",
				name = "plain", 
				picture = "https://avatars3.githubusercontent.com/u/46805717?s=400&u=0fb083d0ea01e2f82a9316849002c20db45146d5&v=4", 
				description = "Old-Fashioned Plain Bagel", 
				price = "$1.99")
	resp, result = h.request(url, 
							  "POST",
							  body=json.dumps(data),
							  headers = {"Content-Type" : "application/json"})
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])
except Exception as err:
	print("Test 2 FAILED: Could not add new bagels")
	print(err.args)
	sys.exit()
else:
	print("Test 2 PASS: Succesfully made new bagels")
print("-----------------------------------------------")

# TEST THREE TRY TO READ BAGELS WITH INVALID CREDENTAILS
try:
	h = Http()
	h.add_credentials('DimaKyn','Youdacity')
	url = address + "/bagels"
	data = dict(username="DimaKyn", 
				password = "youdacity")
	resp, result = h.request(url, 
							 "GET",
							 json.dumps(data))
	if resp["status"] == "200":
		raise Exception("Security Flaw: able to log in with invalid credentials")
except Exception as err:
	print("Test 3 FAILED")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: App checks against invalid credentials")
print("-----------------------------------------------")

# TEST FOUR -- TRY TO READ BAGELS WITH VALID CREDENTIALS
try:
	h = Http()
	h.add_credentials("DimaKyn", "Udacity")
	url = address + "/bagels"
	resp, result = h.request(
							url,
							"GET")
	if resp["status"] != "200":
		raise Exception("Unable to access /bagels with valid credentials")
except Exception as err:
	print("Test 4 FAILED")
	print(err.args)
	sys.exit()
else:
	print("Test 4 PASS: Logged in User can view /bagels")
	print("==================================================")
	print("ALL TESTS PASSED")