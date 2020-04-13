import httplib2
import json
import sys 

print("Running Endpoint Tester...\n")
address = input("Please enter the address of the server you want to \
	access, \n if left blank the connection will set to 'http://localhost:8000'")
if address == "":
	address = "http://localhost:8000"

# Making a Get Request 
print("Making a Get Request for /puppies...")
try:
	url = address + "/puppies"
	h = httplib2.Http()
	resp, result = h.request(url, "GET")
	if resp["status"] != "200":
		raise Exception("Received an unsuccessful status code of %s" % resp["status"])
except Exception as err:
	print("Test 1 FAILED: Could not make GET to web server")
	print("err.args")
	sys.exit()
else:
	print("Test 1 Pass: Succesfuly Made GET Request to /puppies")

# Making GET Requests to /puppies/id
print("Making GET Requests to /puppies/id")
try:
	id = 1
	while id <= 10:
		url = address + "/puppies/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, "GET")
		if resp["status"] != "200":
			raise Exception("Received an unsuccessful status code of %s" % resp["status"])
		id += 1

except Exception as err:
	print("Test 2 FAILED: Could not make GET Request to /puppies/id")
	print(err.args)
	sys.exit()

else:
	print("Test 2 PASS: Succesfully Made GET Request to /puppies/id")
	print("ALL TEST PASSED!!!")