from flask import Flask, abort
from se.Controllers.Auth.LegacyController import LegacyController

class RoutesMiddleware():
    def verify_token(self, access_token):
        token = LegacyController().validate_token(access_token)
        if token.status_code == 200:
            return token 
        abort(401)