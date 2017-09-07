import hashlib
import os
import base64

class PasswordHelper:
	def get_hash(self, plain):
		return hashlib.sha512(plain).hexdigest()

	def get_salt(self):
		return base64.b64encode(os.urandom(20))

	def validate_password(self, plain, salt, expected):
		return self.get_hash(plain + salt) == expected

def test_all():
	pswd = PasswordHelper()
	print(pswd.get_hash("123456"))
	print(pswd.get_salt())
	#print(pswd.validate_password("123456",get_salt(),))

def main():
	test_all()

if __name__ == "__main__":
	main()
