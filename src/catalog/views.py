from django.shortcuts import render

from.models import Tweets

def stream(request):
	all_tweets = Tweets.objects.all()
	
	return render(request, 'catalog/stream.html', {
		'all_tweets': all_tweets,
	})