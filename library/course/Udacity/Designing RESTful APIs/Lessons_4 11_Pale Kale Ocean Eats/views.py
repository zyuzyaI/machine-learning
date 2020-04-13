from models import Base, User 
from flask import Flask, request, url_for, abort, g, render_template, jsonify
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth 
import json

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response 
import requests 

auth = HTTPBasicAuth()

engine = create_engine("sqlite:///userWithOAuth.db", connect_args={'check_same_thread': False})

Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

CLEINT_ID = json.loads(
    open("client_secrets.json", "r").read())["web"]["client_id"]

@auth.verify_password
def verify_password(username_or_token, password):
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user 
    return True 

@app.route("/clientOAuth")
def start():
    return render_template("clientOAuth.html")

@app.route("/oauth/<provider>", methods=["POST"])
def login(provider):
    # STEP 1 - Parse the auth code 
    auth_code = request.json.get("auth_code")
    print("Step 1 - Complete, received auth code %s" % auth_code)
    if provider == "google":
        # Step 2 - Exchange for a token 
        try:
            # Update the authorization code into a credentails object
            oauth_flow = flow_from_clientsecrets("client_secret.json", scope="")
            oauth_flow.redirect_uri = "postmessage"
            credentails = oauth_flow.step2_exchange(auth_code)
        except FlowExchangeError:
            response = make_response(json.dumps("Failed to update the authorization code."), 401)
            response.headers["Content-Type"] = "application/json"
            return response

        # Check that the acces token is valid 
        access_token = credentails.access_token 
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, "GET")[1])
        # If there was an error in the access token info, abort
        if result.get("error") is not None:
            response = make_response(json.dumps(result.get("error")), 500)
            response.headers["Content-Typee"] = "application/json"

        print("Step 2 Complete! Access Token : %s " % credentails.access_token)

        # Step 3 - Find User or make a new one 

        # Get user info 
        h = httplib2.Http()
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentails.access_token, 'alt':'json'}
        answer = requests.get(userinfo_url, params=params)
      
        data = answer.json()

        name = data['name']
        picture = data['picture']
        email = data['email']
        
        #see if user exists, if it doesn't make a new one
        user = session.query(User).filter_by(email=email).first()
        if not user:
            user = User(username = name, picture = picture, email = email)
            session.add(user)
            session.commit()

        #STEP 4 - Make token
        token = user.generate_auth_token(600)

        #STEP 5 - Send back token to the client 
        return jsonify({'token': token.decode('ascii')})
        
        #return jsonify({'token': token.decode('ascii'), 'duration': 600})
    else:
        return 'Unrecoginized Provider'

@app.route("/token")
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({"token": token.decode("ascii")})

@app.route("/users", methods=["POST"])
def new_user():
    username = request.json.get("username")
    password = request.json.get("password")
    if username is None or password is None:
        print("missing arguments")
        abort(400)

    if session.query(User).filter_by(username=username).first() is not None:
        print("existing user")
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'}), 200#, {'Location': url_for('get_user', id = user.id, _external = True)}

    user = User(username = username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'username': user.username }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/api/users/<int:id>')
def get_user(id):
    user = session.query(User).filter_by(id=id).one()
    if not user:
        abort(400)
    return jsonify({'username': user.username})

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })



if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='localhost', port=8000)

