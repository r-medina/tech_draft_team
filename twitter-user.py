from twitter import Twitter, OAuth, TwitterHTTPError
import json, sentiment_analysis

OAUTH_TOKEN = '6015802-ja2jaDc8ZFlRfH7CQKRKknuLjGOs6L7SafJNgfIu5Q'
OAUTH_SECRET = 'v8NwzfbbBmxE2F20eP0XWg9x7ePfyKIuTFMrFo4E4jOd0'
CONSUMER_KEY = '9AmgHI6GRXuffVmPF1xsCBquF'
CONSUMER_SECRET = 'xtVNoWtwEprLkxEJQt6nxNhOOy06Mf31yIsxahZTzJ4D0cvsZm'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

def getStatuses(username):
	statuses = t.GetUserTimeline(username)
	return [s.text for s in statuses]

get_sentiment(getStatuses(username='mumbaikara'))