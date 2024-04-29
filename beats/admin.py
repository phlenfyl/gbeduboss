from django.contrib import admin
from .models import *
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display=('name','slug','created','updated')
    list_display_links=('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Categories, CategoriesAdmin)

# class All_artistAdmin(admin.ModelAdmin):
#     list_display=('name','slug','created','updated')
#     list_display_links=('name',)
#     prepopulated_fields = {'slug': ('name',)}

# admin.site.register(All_artist, All_artistAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display=('name','slug','created','updated')
    list_display_links=('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Genre, GenreAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display=('album_id','name','slug','image','label','catalog','beat_format','tags','descrip','price','category','genre','created','updated')
    list_display_links=('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Album, AlbumAdmin)

class Number_albumAdmin(admin.ModelAdmin):
    list_display=('created_albums','created','updated')
    list_display_links=('created_albums',)

admin.site.register(Number_album, Number_albumAdmin)

class BeatsAdmin(admin.ModelAdmin):
    list_display=('album_name','beats_id','name','subname','slug','label','tags','descrip','price','buy','display','freedownload','image','beats','category','genre','created','updated')
    list_display_links=('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Beats, BeatsAdmin)

class Number_beatAdmin(admin.ModelAdmin):
    list_display=('created_beats','created','updated')
    list_display_links=('created_beats',)

admin.site.register(Number_beat, Number_beatAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('user','comment_beat','playsong_com','name','pics','comment','date','updated')
    list_display_links=('comment',)

admin.site.register(Comment, CommentAdmin)
