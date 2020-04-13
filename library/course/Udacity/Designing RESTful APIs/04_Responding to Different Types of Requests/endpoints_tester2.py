import httplib2
import json
import sys 

print("Running Endpoint Tester...\n")
address = input("Please enter the address of the server you want to access, \n\
	If left blank the connection will be set to 'http://localhost:8000'")
if address == "":
	address = "http://localhost:8000"

# Making a GET Request
print("\n[INFO] Making a GET Request for /puppies...")
try:
	url = address + "/puppies"
	h = httplib2.Http()
	resp, result = h.request(url, "GET")
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])
except Exception as err:
	print("Test 1 FAILED: Coul not make GET Request to web server")
	print(err.args)
	sys.exit()

else:
	print("Test 1 PASS: Succesfully Made GET Request to /puppies")

# Making a post Request 
print("\n[INFO] Making a Post request to /puppies...")
try:
	url = address + "/puppies"
	h = httplib2.Http()
	resp, result = h.request(url, "POST")
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])

except Exception as err:
	print("Test 2 FAILED: Could not make POST Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 2 PASS: Succesfully Made POST Request to '/puppies'")

# Making GET Request to pupies/id
print("\n[INFO] Making GEt requests to /puppies/id")
try:
	id = 1 
	while id <= 10:
		url = address + "/puppies/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, "GET")
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		id += 1
except Exception as err:
	print("Test 3 FAILED: Could not make GET Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Succesfully Made GET Request to '/puppies/id'")

# Making a PUT Request
print("\n[INFO] Making PUT requests to /puppies/id")
try:
	id = 1
	while id <= 10:
		url = address + "/puppies/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, "PUT")
		if resp["status"] != "200":
			raise Exception("Received an unsuccessfull status code of %s" % resp["status"])
		id += 1
except Exception as err:
	print("Test 4 FAILED: Could not make PUT Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 4 PASS: succesfully Made PUT Request to '/puppies/id'")

# Makint a DELETE Request
print("\n[INFO] Making DELETE request to /puppies/id")
try:
	id = 1
	while id <= 10:
		url = address + "/puppies/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, "DELETE")
		if resp["status"] != "200":
			raise Exception("Received an unsuccessful status code of %s" % resp["status"])
		id += 1
except Exception as err:
	print("Test 5 FAILED: Could not Made DELETE Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 5 PASS: SuccesFully Made Request to '/puppies/id'")
	print("-------------------------------------------------------")
	print("ALL TESTS PASSED!!!")