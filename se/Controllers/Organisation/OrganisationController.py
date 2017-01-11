from flask import Flask
from se.Controllers.BaseController import BaseController
from se.Validators.OrganisationValidator import OrganisationValidator
from se.Exceptions.SeException import SeException
from se.Repositories.OrganisationRepository import OrganisationRepository
import flask
import uuid

class OrganisationController():
	
	def __init__(self):
		return

	def register_organisation(self, data, access_token):
		is_validated = OrganisationValidator().register_organisation(data.json)
		if is_validated:
			request = data.json
			value = {'name':request['name'], 'description':request['description'], 'url':request['url'], 'logo':request['logo'], 'type':request['type'], 'apps':request['apps'], 'access_token':access_token}
			result = OrganisationRepository().register_organisation(value)
			if result != False:
				return BaseController().respond(201, result)
			else:
				return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')
				
		else:
			return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Form Input')

	def register_organisation_type(self, data, access_token):
                is_validated = OrganisationValidator().register_organisation_type(data.json)
                if is_validated:
                        request = data.json
                        value = {'name':request['name'], 'description':request['description'], 'access_token':access_token}
                        result = OrganisationRepository().register_organisation_type(value)
                        if result != False:
                                return BaseController().respond(201, result)
                        else:
                                return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')

                else:
                        return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Form Input')
	
			

	def register_apps(self, data, access_token):
		value = []
                is_validated = OrganisationValidator().register_apps(data.json)
                if is_validated:
                        request = data.json
                        value = {'name':request['name'], 'description':request['description'], 'url':request['url'], 'logo':request['logo'], 'access_token':access_token}
                        result = OrganisationRepository().register_apps(value)
                        if result != False:
                                return BaseController().respond(201, result)
                        else:
                                return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')

                else:
                        return SeException().make_error(400, 'SE_IDLegCon400', 'Invalid Form Input')

	def get_all_apps(self, access_token):
                value = {'access_token':access_token}
                result = OrganisationRepository().get_all_apps(value)
                if result != False:
                        return BaseController().respond(200, result)
                else:
                        return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')

	def get_all_organisation_type(self, access_token):
                value = {'access_token':access_token}
                result = OrganisationRepository().get_all_organisation_type(value)
                if result != False:
                        return BaseController().respond(200, result)
                else:
                        return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')
	def get_all_organisation(self, access_token):
                value = {'access_token':access_token}
                result = OrganisationRepository().get_all_organisation(value)
                if result != False:
                        return BaseController().respond(200, result)
                else:
                        return SeException().make_error(401, 'SE_IDLegCon401', 'Unauthorized User')

