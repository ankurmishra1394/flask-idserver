from flask import Flask, abort
from se.Repositories.Repository import Repository
from se.Exceptions.SeException import SeException
import datetime
import json
import bcrypt
import uuid
class OrganisationRepository():

        def register_apps(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
                if user['is_god']:
                        del data['access_token']
                        user_detail = {'id':user['id'], 'display_name':user['display_name'], 'email':user['email']}
                        data['created_by'] = json.dumps(user_detail)
                        params = {'id':str(uuid.uuid4()).strip(), 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                        params.update(data)
                        newParam = Repository().store('apps', params)
                        return Repository().fetchDetailsWithoutJoin('apps', newParam)
                else:
                        return False
        def register_organisation_type(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
                if user['is_god']:
                        del data['access_token']
                        user_detail = {'id':user['id'], 'display_name':user['display_name'], 'email':user['email']}
                        data['created_by'] = json.dumps(user_detail)
                        params = {'id':str(uuid.uuid4()).strip(), 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                        params.update(data)
                        newParam = Repository().store('organisation_type', params)
                        return Repository().fetchDetailsWithoutJoin('organisation_type', newParam)
                else:
                        return False
	def register_organisation(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
		if user['is_god']:
                        del data['access_token']
                        user_detail = {'id':user['id'], 'display_name':user['display_name'], 'email':user['email']}
                        data['created_by'] = json.dumps(user_detail)
                        params = {'id':str(uuid.uuid4()).strip(), 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                        params.update(data)
                        for app in params['apps']:
                                isExist = Repository().fetchDetailsWithoutJoin('apps', {'id':app})
                                if len(isExist) == 0:
                                        abort(400)
                        for typeId in params['type']:
                                isExist = Repository().fetchDetailsWithoutJoin('organisation_type', {'id':typeId})
                                if len(isExist) == 0:
                                        abort(400)
                        type = data['type']
                        del params['type']
                        apps = data['apps']
                        del params['apps']
                        newParam = Repository().store('organisation', params)
                        for app in data['apps']:
                                appParam = {'id':str(uuid.uuid4()).strip(), 'app_id':app.strip(), 'organisation_id':newParam['id'], 'created_by':data['created_by'], 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                                store = Repository().store('organisation_apps', appParam)
                        for typeId in data['type']:
                                typeParam = {'id':str(uuid.uuid4()).strip(), 'organisation_type_id':typeId.strip(), 'organisation_id':newParam['id'], 'created_by':data['created_by'], 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                                store = Repository().store('organisation_organisation_type', typeParam)
                        return Repository().fetchDetailsWithoutJoin('organisation', newParam)
                        
		else:
			return False

        def get_all_apps(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
                if user['is_god']:
                        newParam = {}
                        return Repository().fetchDetailsWithoutJoin('apps', newParam)
                return False

        def get_all_organisation_type(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
                if user and user['is_god']:
                        newParam = {}
                        return Repository().fetchDetailsWithoutJoin('organisation_type', newParam)
                return False

        def get_all_organisation(self, data):
                joinOn = {'user_token.user_id':'users.id'} 
                params = {'user_token.access_token':str(data['access_token'])} 
                user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
                if user['is_god']:
                        newParam = {}
                        joinOn = {'organisation.id':'organisation_organisation_type.organisation_id'} 
                        return Repository().fetchDetailsWithJoin('organisation', 'organisation_organisation_type', joinOn, newParam)
                return False
	
