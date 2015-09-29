from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from PIL import Image 
import os 
from settings import MEDIA_ROOT 


class Album(models.Model):
	title = models.CharField(max_length=60)
	public = models.BooleanField(default=False)

	def __str__(self):
		return self.title 

class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.FileField(upload_to="images/")
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	albums = models.ManyToManyField(Album, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

	# I'm not really sure what this is doing
	# Resizing the image, somehow 
	# http://lightbird.net/dbe/photo.html
	def save(self, *args, **kwargs):
		super(Image, self).save(*args, **kwargs)
		im = Image.open(os.path.join(MEDIA_ROOT, self.image.name))
		self.width, self.height = im.size
		super(Image, self).save(*args, **kwargs)

	def size(self):
		return "%s x %x" % (self.width, self.height)

	def __str__(self):
		return self.image.name

	def albums_(self):
		lst = [x[1] for x in self.albums.values_list()]
		return str(join(lst, ', '))

	#this doesn't make any sense either 
	def thumbnail(self):
          return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % ((self.image.name, self.image.name))
                                                              

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title"]

class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__str__", "title", "user", "size", "albums_", "thumbnail"]
	list_filter = ["albums", "user"]

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()




