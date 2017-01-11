from flask import Flask
from validate_email import validate_email

class OrganisationValidator():
	
	def __init__(self):
		return 

	def register_organisation(self, data):

		if 'name' not in data:
			return False
		if 'logo' not in data:
			return False
		if 'url' not in data:
			return False
		if 'type' not in data:
			return False
		if len(data['type']) == 0:
			return False
		if 'apps' not in data:
			return False
		if len(data['apps']) == 0:
			return False
		return True

	def register_apps(self, data):
		if 'name' not in data:
                        return False
                if 'logo' not in data:
                        return False
                if 'url' not in data:
                        return False
                return True
		

	def register_organisation_type(self, data):
                if 'name' not in data:
                	return False
                return True

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


