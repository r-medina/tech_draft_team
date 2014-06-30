import requests

'''
	Returns a dictionary {'confidence': _____, 'result': _____}
	returns None if corrupted data or connection error
'''

def get_sentiment(text):
	r = requests.post("http://sentiment.vivekn.com/web/text/", data={'txt': text})
	if r.status_code != 200:
		return None
	response = r.json()
	del response['sentence']
	if 'confidence' not in response or 'result' not in response:
		return None
	return response