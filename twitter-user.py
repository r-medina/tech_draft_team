import twitter
import json, sentiment_analysis

OAUTH_TOKEN = '6015802-ja2jaDc8ZFlRfH7CQKRKknuLjGOs6L7SafJNgfIu5Q'
OAUTH_SECRET = 'v8NwzfbbBmxE2F20eP0XWg9x7ePfyKIuTFMrFo4E4jOd0'
CONSUMER_KEY = '9AmgHI6GRXuffVmPF1xsCBquF'
CONSUMER_SECRET = 'xtVNoWtwEprLkxEJQt6nxNhOOy06Mf31yIsxahZTzJ4D0cvsZm'

t = twitter.Api(consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=OAUTH_TOKEN,
    access_token_secret=OAUTH_SECRET)

def getStatuses(username):
	statuses = t.GetUserTimeline(username)
	texts = [s.text for s in statuses]
        combinedText = "".join(texts)
        return combinedText

print sentiment_analysis.get_sentiment(getStatuses(username='mumbaikara'))
