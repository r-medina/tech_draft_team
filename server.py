from flask import Flask, request, make_response
app = Flask(__name__)
import twitter
import twitter2
from website import website_sentiment

@app.route("/", methods = ['POST'])
def get_data():
	# Get information in request.form
  string = ""
  string += twitter2.getStatuses(request.form['twitter'])
  string += website_sentiment(request.form['website'])
  return make_response(string, 200)

if __name__ == '__main__':
	app.run(port=8000, debug=True)
