import os
from datetime import datetime

from django.db import models

class Hashtags(models.Model):
	tag = models.CharField(max_length=50, null=False, blank=False)

class Tweets(models.Model):
	username = models.CharField(max_length=25, null=False, blank=False)
	text = models.TextField(null=False, blank=False)
	tweet_id = models.BigIntegerField(default=0, null=False, blank=False)
	tweet_date = models.DateTimeField(null=False, blank=False, default=datetime.now)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)