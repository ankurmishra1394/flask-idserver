from flask import Flask
import flask

class SeException():
	
	def make_error(self, status_code, se_code, message):
    		response = flask.jsonify({
        			'code': status_code,
				'data':[],
				'notification': {
                                                'hint':message,
                                                'message':message,
                                                'seCode': se_code,
                                                'type':'error'
                                        }
   	 		})
    		response.status_code = status_code
    		return response	
