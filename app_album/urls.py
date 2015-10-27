from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
	url(r'^image/(?P<pk>[0-9]+)/$', views.image_detail, name='image_detail'),
	url(r'^login/$', views.login, name="login"),
	url(r'^logout/$', views.logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	




