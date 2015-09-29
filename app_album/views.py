from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
		return render(request, 'app_album/index.html', {})
