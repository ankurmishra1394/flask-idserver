from flask import Flask, abort
from se.Repositories.Repository import Repository
from se.Models.Users import Users
import datetime
import json
import bcrypt
import uuid
import jwt
class LegacyRepository():
    
    def signup_user(self, data):
        isUserExist = Repository().fetchDetailsWithoutJoin('users', {'email':data['email']})
        if isUserExist:
            abort(409)
        joinOn = {'user_token.user_id':'users.id'} 
        params = {'user_token.access_token':str(data['access_token'])} 
        user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
        if user['is_god']:
            user_detail = {'id':user['id'], 'display_name':user['display_name'], 'email':user['email']}
            params = {'id':str(uuid.uuid4()).strip(), 'is_god':False, 'is_admin':False, 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
            del data['access_token']
            org_id = data['org_id']
            del data['org_id']
            params.update(data)
            newParam = Repository().store('users', params)
            if newParam:
                org_user_param = {'id':str(uuid.uuid4()).strip(), 'organisation_id':org_id, 'user_id':newParam['id'],'created_by':json.dumps(user_detail), 'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now()}
                Repository().store('organisation_user', org_user_param)
            return Repository().fetchDetailsWithoutJoin('users', newParam)
        else:
            return False

    def login_user(self, data):
        params = {'email':str(data['email'])}
        user = Repository().fetchDetailsWithoutJoin('users', params)
        if user and bcrypt.checkpw(data['password'], user['password']):
            toCheck = Repository().fetchDetailsWithoutJoin('user_token', {'user_id':user['id']})
            if toCheck:
                params = {'access_token':(bcrypt.hashpw(str(datetime.datetime.now()), bcrypt.gensalt())), 'updated_at':datetime.datetime.now(), 'expires_at':str(datetime.datetime.now()+ datetime.timedelta(days=7))}
                generateNewAccessToken = Repository().update('user_token', params, {'user_id':user['id']})
                return params
            else:
                public_key = jwt.encode({"id":str(user['id']),"displayName":str(user['display_name']), "email":str(user['email'])}, 'SE_ID_1131_SERVER', algorithm='HS256')
                params = {'id':str(uuid.uuid4()).strip(), 
                'user_id':user['id'], 'public_key': public_key, 'private_key':str(uuid.uuid4()).strip(), 
                'access_token':(bcrypt.hashpw(str(datetime.datetime.now()), bcrypt.gensalt())),
                'created_at':datetime.datetime.now(), 'updated_at':datetime.datetime.now(), 
                'expires_at':str(datetime.datetime.now()+ datetime.timedelta(days=7))
                }
                generateNewAccessToken = Repository().store('user_token', params)
                return Repository().fetchDetailsWithoutJoin('user_token', {'id':generateNewAccessToken['id']})

    def validate_token(self, data):
        params = {'access_token':data['access_token']}
        user = Repository().fetchDetailsWithoutJoin('user_token', params)
        if len(user):
            return user
        else:
            return False
    
    def update_account_password(self, data):
        joinOn = {'user_token.user_id':'users.id'} 
        params = {'user_token.access_token':str(data['access_token'])} 
        user = Repository().fetchDetailsWithJoin('user_token', 'users', joinOn, params)
        if user and bcrypt.checkpw(str(data['current_password']), str(user['password'])):
            logoutUser = self.logout_user({'access_token':data['access_token']})
            if logoutUser:
                params = {'password':bcrypt.hashpw(str(data['new_password']), bcrypt.gensalt()), 'updated_at':datetime.datetime.now()}
                updatePassword = Repository().update('users', params, {'id':user['user_id']})
                if updatePassword:
                    return True
                else:
                    return False
            else:
                return False
        else:
            abort(401)

    def logout_user(self, data):
        token = self.validate_token({'access_token':data['access_token']})
        params = {'access_token':None, 'updated_at':datetime.datetime.now(), 'expires_at':str(datetime.datetime.now()+ datetime.timedelta(days=7))}
        logoutUser = Repository().update('user_token', params, {'id':token['id']})
        if logoutUser:
            return True
        else:
            return False

    def reset_account_password(self, data):
        params = {'id':data['user_id']}
        user = Repository().fetchDetailsWithoutJoin('users', params)
        if user and user['master_password'] == data['master_password']:
            params = {'password':bcrypt.hashpw(str(data['new_password']), bcrypt.gensalt()), 'updated_at':datetime.datetime.now(), 'master_password':None, 'key_expire':None}
            updatePassword = Repository().update('users', params, {'id':user['id']})
            if updatePassword:
                params = {'access_token':None, 'updated_at':datetime.datetime.now(), 'expires_at':str(datetime.datetime.now()+ datetime.timedelta(days=7))}
                logoutUser = Repository().update('user_token', params, {'id':token['id']})
                if logoutUser:
                    return True
                else:
                    params = {'password':user['password'], 'updated_at':datetime.datetime.now(), 'master_password':None, 'key_expire':None}
                    updatePassword = Repository().update('users', params, {'id':user['id']})
        return False








