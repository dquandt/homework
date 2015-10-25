from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Album, Image
from django.core.urlresolvers import reverse 

def index(request):
	albums = Album.objects.all()
	return render(request, 'app_album/index.html', {'albums' : albums})

def album_detail(request, pk):
	album = get_object_or_404(Album, pk=pk)
	images = album.image_set.all()
	return render(request, 'app_album/album_detail.html', {'album': album, 'images': images})

def image_detail(request, pk):
	image = get_object_or_404(Image, pk=pk)
	return render(request, 'app_album/image_detail.html', {'image': image})



