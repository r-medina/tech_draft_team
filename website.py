from bs4 import BeautifulSoup
import requests
import sys
from sentiment_analysis import get_sentiment
def website_sentiment(url):
  site = requests.get(url)
  soup = BeautifulSoup(site.text)
  return get_sentiment(soup.get_text())
