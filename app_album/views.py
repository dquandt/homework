from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Album 

def index(request):
		albums = Album.objects.all()
		return render(request, 'app_album/index.html', {'albums' : albums})
