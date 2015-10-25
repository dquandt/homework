from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from PIL import Image 
import os 
from django.utils import timezone

class Album(models.Model):
	title = models.CharField(max_length=60)
	public = models.BooleanField(default=False)
	author = models.ForeignKey('auth.User')

	def __str__(self):
		return self.title 

class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.FileField(upload_to="images/")
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	albums = models.ManyToManyField(Album, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

	def __str__(self):
		return self.title

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title"]

class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__str__", "title", "user"]
	list_filter = ["albums", "user"]




