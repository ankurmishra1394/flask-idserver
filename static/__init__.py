from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/yes/<int:score>')
def hello_name(score):
	return render_template('home.html', marks=score)

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template('result.html', result = result)

@app.route("/")
def hello():
	return render_template('score.html')

@app.errorhandler(500)
def internal_error(error):
	return "500"

if __name__ == "__main__":
	app.run()
