from flask import Flask, render_template, request
import os, sys
sys.path.append('..')
sys.path.append(os.path.dirname(__file__))
app = Flask(__name__)
app.config.update(DEBUG=True)
from se.Routes.Auth.routes import auth
from se.Routes.Organisation.routes import orgs
app.register_blueprint(auth)
app.register_blueprint(orgs)

@app.route("/")
def hello():
	return render_template('score.html')


if __name__ == '__main__':
	app.run()
