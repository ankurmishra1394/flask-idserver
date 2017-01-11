from flask import Flask, Blueprint, request
from flask_mail import Mail, Message

app=Flask(__name__)
auth=Blueprint('auth', __name__, url_prefix='/auth/')

class Mailer():

	def __init__(self):
		return


	def mail(self, mail_subject, mail_recipients, mail_body):
		
		app.config['MAIL_SERVER']='smtp.mailgun.org'
                app.config['MAIL_PORT'] = 587
                app.config['MAIL_USERNAME'] = 'postmaster@notify.sourceeasy.com'
                app.config['MAIL_PASSWORD'] = '5m6sb6ru42i3'
                app.config['MAIL_USE_TLS'] = True
                app.config['MAIL_USE_SSL'] = False
                mail = Mail(app)
	
		msg = Message(mail_subject, sender = 'no-reply@sourceeasy.com', recipients = mail_recipients)
   		msg.body = mail_body
   		sent = mail.send(msg)
   		if sent:
			return True
		else:
			return False
