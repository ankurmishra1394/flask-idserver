from flask import Flask, make_response
import flask

class BaseController():

	
	def respond(self, status_code, data):
                response = flask.jsonify({
                                'notification': {
						'hint':'Reponse Sent',
						'message':'Success',
						'seCode':'SE_200',
						'type':'success'
					},
                                'data': data,
                        })
                response.status_code = status_code
                return response
