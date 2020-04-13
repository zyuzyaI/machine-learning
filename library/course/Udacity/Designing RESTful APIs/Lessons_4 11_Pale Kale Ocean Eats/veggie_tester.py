from httplib2 import Http
import json
import sys 

print("Running Endpoint Tester...\n")
address = input("Please enter the address of the server you want to acces, \n\
	If left blank the connection will be set to 'http://localhost:8000'")
if address == "":
	address = "http://localhost:8000"

# GET AUTH CODE
client_url = address + "/clientOAth"
print("VISIT %s in your browser" % client_url)
auth_code = ""
while auth_code == "":
	auth_code = input("Paste the One-Time Auth Code Here")

# TEST ONE -- GET TOKEN 
try:
	h = Http()
	url = address + "/outh/google"
	data = dict(auth_code=auth_code)
	data = json.dumps(data)
	resp, result = h.request(url, 
							 "POST", 
							 body=data,
							 headers={"Content-Type":"application/json"}
							)
	if resp["status"] != "200":
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	new_result = json.loads(result)
	if not new_result["token"]:
		raise Exception('No Token Received!')
	token = new_result["token"]
except Exception as err:
	print("Test 1 FAILED: Could not exchange auth code for a token")
	print(err.args)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully obtained token")

