from flask import Flask, Blueprint, request
#from se.Controllers.Auth.LegacyController import LegacyController
from se.Controllers.Organisation.OrganisationController import OrganisationController
from se.Middleware.RoutesMiddleware import RoutesMiddleware

app=Flask(__name__)

orgs = Blueprint('orgs', __name__, url_prefix='/admin/')

#legacy = LegacyController()
organisation = OrganisationController()


@orgs.route('orgs/register', methods=['POST'])
def register_organisation():
	is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
	if is_validated:
		result = organisation.register_organisation(request, request.headers.get('access_token'))
		return result
	
@orgs.route('app/register', methods=['POST'])
def register_apps():
        is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
        	result = organisation.register_apps(request, request.headers.get('access_token'))
        	return result

@orgs.route('orgs/type/register', methods=['POST'])
def register_organisation_type():
        is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
                result = organisation.register_organisation_type(request, request.headers.get('access_token'))
                return result

@orgs.route('apps', methods=['GET'])
def get_all_apps():
        is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
                result = organisation.get_all_apps(request.headers.get('access_token'))
                return result

@orgs.route('orgs/type', methods=['GET'])
def get_all_organisation_type():
        is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
                result = organisation.get_all_organisation_type(request.headers.get('access_token'))
                return result

@orgs.route('orgs', methods=['GET'])
def get_all_organisation():
        is_validated = RoutesMiddleware().verify_token(request.headers.get('access_token'))
        if is_validated:
                result = organisation.get_all_organisation(request.headers.get('access_token'))
                return result

