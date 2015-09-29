from django.contrib import admin
from .models import Album, AlbumAdmin, Image, ImageAdmin

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)

