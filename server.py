from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def get_data():
	# Get information in request.form
	return make_response('Hello World', 200)

if __name__ == '__main__':
	app.run(port=8000, debug=True)
