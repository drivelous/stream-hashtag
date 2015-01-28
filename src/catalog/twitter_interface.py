from .models import Tweets

from authorization import API as api

results = api.search.tweets(q="#WhatSoNot")
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

for status in statuses:
    tweet = Tweets(text=status['text'],
                    username=status['user']['screen_name'],
                    tweet_id=status['id'])
    tweet.save()