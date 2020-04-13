from httplib2 import Http 
import base64 
import json 
import sys

print("Running Endpoint Tester...")
address = input("Please enter the address of the server you want to access, \n\
	If left blank the connection will be set to 'http://localhost:8000':")

if address == "":
	address = "http://localhost:8000"

# TEST ONE -- TRY TO REGISTER A NEW USER 
try:
	h = Http()
	url = address + "/users"
	data = dict(username="Flask", password="Flask")
	data = json.dumps(data)
	resp, result = h.request(url,
							"POST",
							body=data,
							headers={"Content-Type": "application/json"}
							)
	if resp["status"] != "201" and resp["status"] != "200":
		raise Exception("'Received an unsuccessful status code of %s" % resp['status'])
except Exception as err:
	print("Test 1 FAILED: Could not make a new user")
	print(err.args)
	sys.exit()
else:
	print("TEst 1 PASS: Succesfully made a new user")
	print("--------------------------------------------------")

# TEST TWO -- OBTAIN A TOKEN
try:
	h = Http()
	h.add_credentials("Flask", "Flask")
	url = address + "/token"
	resp, result = h.request(url,
							"GET",
							headers={"Content-Type": "application/json"})
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])
	new_result = json.loads(result)
	if not new_result["token"]:
		raise Exception("No Tocken Received!")
	token = new_result["token"]
	print("received token %s" % token)
except Exception as err:
	print("Test 2 FAILED: Could not exchange user credentails for a token")
	print(err.args)
	sys.exit()
else:
	print("Test 2 PASS: Succesfully obtained TOKEN!")
	print("-----------------------------------------")

# TEST THREE -- TRY TO ADD PRODUCTS TO DATABASE
try:
	h = Http()
	h.add_credentials(token, "blank")
	url = address + "/products"
	data = dict(name="apple", category="fruit", price="$0.99")
	data = json.dumps(data)
	resp, result = h.request(url,
							"POST",
							body=data,
							headers={"Content-Type": "application/json"})
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code %s" % resp["status"])
except Exception as err:
	print("Test 3 FAILED: Could not add new products")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Succesfully added new products")
	print("---------------------------------------------")

# TEST FOUR -- TRY ACCESSING ENDPOINT WITH AN INVALID TOKEN
try:
	h = Http() 
	h.add_credentials('Dima','Wrong')
	url = address + '/token'
	resp, result = h.request(url,
							 'GET',
							 headers={"Content-Type" : "application/json"})
	if resp['status'] == '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 4 FAILED: Could not cheching invalid token")
	print(err.args)
	sys.exit()
else:
	print("Test 4 PASS: Succesfully checking invalid token!")
	print("-------------------------------------------------")

# TEST FIVE -- TRY TO VIEW ALL PRODUCTS IN DATABASE
try:
	h = Http()
	h.add_credentials("Flask", "Flask")
	url = address + "/products"
	resp, result = h.request(url,
							"GET",
							headers={"Content-Type": "application/json"})
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp['status'])
except Exception as err:
	print("Test 5 FAILED: Could not view all products")
	print(err.args)
	sys.exit()
else:
	print("Test 5 PASS: Succesfully view all products!")
	print("---------------------------------------------------")

# TEST SIX -- TRY TO VIEW A SPECIFIC GATEGORY OF PRODUCTS
# try:
# 	h = Http()
# 	url = address + "/products/category"
# 	resp, result = h.request(url,
# 							"GET",
# 							headers={"Content-Type": "application/json"})
# 	if resp["status"] != "200":
# 		raise Exception("Received an unsuccessful status code of %s" % resp['status'])
# except Exception as err:
# 	print("Test 6 FAILED: Could not view specific categories of products")
# 	print(err.args)
# 	sys.exit()
# else:
# 	print("Test 6 PASS: Succesfully view view specific categories of products!")
# 	print("--------------------------------------------------")