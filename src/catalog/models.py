import os
from django.db import models

class Tweets(models.Model):
	username = models.CharField(max_length=25, null=False, blank=False)
	text = models.TextField(null=False, blank=False)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
	url = models.CharField(max_length= 200, null=True, blank=True)