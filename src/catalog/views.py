from django.shortcuts import render

def stream(request):
	return render(request, 'catalog/stream.html',
		{}
	)