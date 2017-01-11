from flask import Flask, Blueprint, request
from se.Controllers.Auth.LegacyController import LegacyController
from se.Middleware.RoutesMiddleware import RoutesMiddleware

app=Flask(__name__)

legacy = LegacyController()

auth=Blueprint('auth', __name__)

@auth.route('/orgs/<org_id>/users', methods=['POST'])
def register_user(org_id):
	is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
        	result = legacy.register_user(request, org_id, request.headers.get('access_token'))
        	return result

@auth.route('/auth/token', methods=['GET'])
def validate_token():
        result = legacy.validate_token(request.headers.get('access_token'))
        return result

@auth.route('/auth/signin', methods=['POST'])
def login_user():
        result = legacy.login_user(request)
        return result

@auth.route('/auth/account/changepassword', methods=['PUT'])
def update_account_password():
	result = legacy.update_account_password(request, request.headers.get('access_token'))
	return result

@auth.route('/auth/account/forgetpassword', methods=['POST'])
def forget_account_password():
	result = legacy.forget_account_password(request)
	return result

@auth.route('/auth/account/<user_id>/resetpassword', methods=['POST'])
def reset_account_password(user_id):
	result = legacy.reset_account_password(user_id, request)
	return result

@auth.route('/auth/signout', methods=['GET'])
def logout_user():
	result = legacy.logout_user(request.headers.get('access_token'))
	return result
