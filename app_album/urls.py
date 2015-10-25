from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.album_list, name='album_list'),
	url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
	url(r'^image/(?P<pk>[0-9]+)/$', views.image_detail, name='image_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	



