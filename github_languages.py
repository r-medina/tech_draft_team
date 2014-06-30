import requests

def get_languages(username):
	r = requests.get('http://osrc.dfm.io/%s.json' % (username, ))
	if r.status_code != 200:
		return []
	data = r.json()
	try:
		languages = data['usage']['languages']
		return [language['language'] for language in languages]
	except KeyError:
		return []

print get_languages('aniruddhc1')