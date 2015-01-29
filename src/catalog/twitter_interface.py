import time

from .models import Tweets

from authorization import API as api

results = api.search.tweets(q="%\23WhatSoNot", count=20)
statuses = results['statuses']


# ##TEXT
# for status in statuses:
# 	print status['text']

#USERNAME
# for status in statuses:
# 	print status['user']['screen_name']

#ID
# for status in statuses:
# 	print status['id']

"""
Write a script that:
-Takes latest entry in DB and gets its id
-Takes the last 20 tweets from Twitter
-Saves every one of those tweets until it gets to the one
with the same id

"""



def get_latest_tweets():
	results = api.search.tweets(q="%\23WhatSoNot", count=20)
	statuses = results['statuses']
	latest = Tweets.objects.latest('tweet_date')

	for status in statuses:
		if status['id'] != int(latest.tweet_id):
			ts = time.strftime('%Y-%m-%d %H:%M:%S',
					time.strptime(status['created_at'],
						'%a %b %d %H:%M:%S +0000 %Y'))

			tweet = Tweets(text=status['text'],
							username=status['user']['screen_name'],
							tweet_id=status['id'],
							tweet_date=ts)
			tweet.save()
			print "I can do stuff"
			print status['created_at']
			print
		else:
			print "gotta break"
			print status['text']
			return

def do_this():
	results = api.search.tweets(q="%\23WhatSoNot", count=20)
	statuses = results['statuses']
	for status in statuses:
		ts = time.strftime('%Y-%m-%d %H:%M:%S',
				time.strptime(status['created_at'],
					'%a %b %d %H:%M:%S +0000 %Y'))

		tweet = Tweets(text=status['text'],
						username=status['user']['screen_name'],
						tweet_id=status['id'],
						tweet_date=ts)
		tweet.save()