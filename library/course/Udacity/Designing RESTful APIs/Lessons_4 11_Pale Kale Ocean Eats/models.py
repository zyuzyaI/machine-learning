from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy import create_engine 
from passlib.apps import custom_app_context as pwd_context 
import random, string 
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	username = Column(String(32), index=True)
	picture = Column(String)
	email = Column(String)
	password_hash = Column(String(64))

	def hash_password(self, password):
		self.password_hash = pwd_context(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password)

	def generate_auth_token(self, expiration=600):
		s = Serializer(secret_key, expires_in=expiration)
		return s.dumps({"id": self.id})

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(secret_key)
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None # Valid token, but expired
		except BadSignature:
			return None # Invalid token
		user_id = data["id"]
		return user_id 

engine = create_engine("sqlite:///paleKate.db")

Base.metadata.create_all(engine)