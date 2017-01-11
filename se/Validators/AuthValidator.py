from flask import Flask
from validate_email import validate_email

class AuthValidator():
	
	def __init__(self):
		return 

	def user_signup(self, data):

		if 'email' not in data:
			return False
		if 'password' not in data:
			return False
		if 'display_name' not in data:
			return False
		# if self.validate_email(data['email']) == False:
		# 	return False
		return True

	def user_login(self, data):
		
		if 'email' not in data:
                        return False
                if 'password' not in data:
                        return False
		if self.validate_email(data['email']) == False:
                        return False
		return True

	def validate_email(self, email):
		is_email = validate_email(str(email), check_mx=True)
                if is_email == True:
                	return True
                else:
                	return False

	def validate_token(self, email):
		if email == None:
			return False
		return True

	def verify_changepassword(self, data):
		if 'currentPassword' not in data:
			return False
		if 'newPassword' not in data:
			return False
		if data['currentPassword'] == data['newPassword']:
			return False
		
		return True


