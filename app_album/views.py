from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Album, Image, User
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

def index(request):
	albums = Album.objects.all()
	return render(request, 'app_album/index.html', {'albums' : albums})

# def login(request):
# 	return render(request, 'app_album/login.html');
	# next = request.GET.get('next', '/')
	# if request.method == "POST":
	# 	username = request.POST['username']
	# 	password = request.POST['password']
	# 	user = authenticate(username=username, password=password)

	# 	if user is not None:
	# 		if user.is_active:
	# 			login(request, user)
	# 			return HttpResponseRedirect(next)
	# 		else:
	# 			return HttpResponse("You shall not pass.")
	# 	else: 
	# 		return HttpResponseRedirect(settings.LOGIN_URL)
	# return render(request, "/login.html", {'redirect_to': next})

def logout(request):
	logout (request)
	return HttpResponseRedirect(settings.LOGIN.URL)

# @login_required
def album_detail(request, pk):
	album = get_object_or_404(Album, pk=pk)
	images = album.image_set.all()
	return render(request, 'app_album/album_detail.html', {'album': album, 'images': images})

def image_detail(request, pk):
	image = get_object_or_404(Image, pk=pk)
	return render(request, 'app_album/image_detail.html', {'image': image})



