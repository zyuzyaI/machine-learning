import httplib2
import json
import sys 

print("[INFO] Running Endpoin Tester...\n")
address = input("Please enter the address of the server you want to access, \n\
	If left blank the connection will be set to 'http://localhost:8000'")
if address == "":
	address = "http://localhost:8000"

# Making a POST Request
print("\n[INFO] Making a POST Request to '/puppies'")
try:
	url = address + "/puppies?name=Fido&description=Playful+Little+Puppy"
	h = httplib2.Http()
	resp, result = h.request(url, 'POST')
	obj = json.loads(result)
	puppyID = obj['Puppy']['id']
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 1 FAILED: Could not make POST Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully Made POST Request to /puppies")

# Making a GET Request
print("\n[INFO] Making a GET Request for /puppies..")
try:
	url = address + "/puppies"
	h = httplib2.Http()
	resp, result = h.request(url, 'GET')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 2 FAILED: Could not make GET Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 2 PASS: Succesfully Made GET Request to /puppies")

# aking GET Requests to /puppies/id
print("\n[INFO] Making GET Requests to /puppies/id")
try:
	id = puppyID
	url = address + "/puppy/%s" % id 
	h = httplib2.Http()
	resp, result(url, "GET")
	if resp["status"] != "200":
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 3 FAILED: Could not make GET Requests to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Succesfully Made GET Request to /puppies/id")

# Making a PUT Request
print("\n[INFO] aking a PUT Request to '/puppies/id'")
try:
	id = puppyID 

	url = address + "/puppies/%s?name=wilma&description=A+sleepy+bundle+of+joy" % id 
	h = httplib2.Http()
	resp, result = h.request(url, 'PUT')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print("Test 4 FAILED: Could not make PUT Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 4 PASS: Succesfully Made PUT Request to /puppies/id")

#Making a DELETE Request
print("\n[INFO] Making DELETE requests to /puppies/id ... ")

try:
	id = puppyID
	url = address + "/puppies/%s" % id 
	h = httplib2.Http()
	resp, result = h.request(url, 'DELETE')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	

except Exception as err:
	print("Test 5 FAILED: Could not make DELETE Requests to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 5 PASS: Succesfully Made DELETE Request to /puppies/id")
	print("ALL TESTS PASSED!!")