from flask import Flask
from se.Controllers.BaseController import BaseController
from se.Validators.AuthValidator import AuthValidator
from se.Exceptions.SeException import SeException
from Mailer import Mailer
from se.Repositories.LegacyRepository import LegacyRepository
import bcrypt
import uuid
import datetime

class LegacyController():
	def __init__(self):
		return
	def register_user(self, data, org_id, access_token):
		# is_validated = AuthValidator().user_signup(data.json)
		is_validated = True
		if is_validated == True:
			request = data.json
			value = {'display_name':str(request['display_name']), 'email':str(request['email']), 'password':bcrypt.hashpw(str(request['password']), bcrypt.gensalt()), 'org_id':str(org_id), 'access_token':str(access_token)}
			result = LegacyRepository().signup_user(value)
			if result:
				return BaseController().respond(201, result)
			elif result == False:
				return SeException().make_error(409, 'SE_IDLegCon409', 'User Already Exists')
			else:
				return result
				
		else:
			return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Form Input')

	def login_user(self, credentials):

		# is_validated = AuthValidator().user_login(credentials.json)
		is_validated = True
		if is_validated == True:
			request = credentials.json
			value = {'email':str(request['email']), 'password':str(request['password'])}
			result = LegacyRepository().login_user(value)
			if result:
				return BaseController().respond(200, result)
			else:
				return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')
		else:
			return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Input Provided')
	
	def validate_token(self, token):
		is_validated = AuthValidator().validate_token(token)
		if is_validated:
			value = {'access_token':str(token)}
			result = LegacyRepository().validate_token(value)
			if result:
				return BaseController().respond(200, result)
			else:
				return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')
		else:
			return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Request')

	def update_account_password(self, data, access_token=None):

		is_validated = AuthValidator().verify_changepassword(data.json)
		if is_validated == True:
			token_validated = self.validate_token(access_token)
			if str(token_validated.status) != '200 OK':
				return token_validated
			request = data.json
			value = {'current_password':str(request['currentPassword']), 'new_password':str(request['newPassword']), 'access_token':access_token}
			result = LegacyRepository().update_account_password(value)
                        if result:
                                return BaseController().respond(200, 'Password Updated')
                        else:
                                return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')
                else:
                        return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Request')

	def logout_user(self, access_token):
		token_validated = self.validate_token(access_token)
               	if str(token_validated.status) != '200 OK':
			return token_validated
		value = {'access_token':access_token}
		result = LegacyRepository().logout_user(value)
		if result:
			return BaseController().respond(200, 'User Logged Out')
		else:
			return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')

	def forget_account_password(self, data):
		request = data.json
		is_validated = AuthValidator().validate_email(str(request['email']))
		if is_validated == True:
			value = [str(request['email'])]
			result = LegacyRepository().forget_account_password(value)
			if result:
				send = Mailer().mail('Forget password request', [str(request['email'])], "You are getting this mail as because you have have requested for forget password help.Please use the master key "+result+" to reset your password. This password will expire within one hour.<br><br> Regards, <br> Sourceeasy Team")
				return BaseController().respond(200, 'Mail sent to your email. Please Check')
			else:
				return SeException().make_error(404, 'SE_IDLegCon404', 'User doesnot exists!')

	def reset_account_password(self, data, user_id):
		if user_id == True:
			value = {'user_id':str(user_id), 'new_password':data['newPassword'], 'master_password':data['masterKey']}
			result = LegacyRepository().reset_account_password(value)
			if result:
				return BaseController().respond(200, 'Password Reset Done. Please Login Again!')
			else:
				return SeException().make_error(401, 'SE_IDLegCon401', 'Authentication Failed!')
