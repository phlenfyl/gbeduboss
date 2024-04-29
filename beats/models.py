from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length= 50)
    slug= models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class All_artist(models.Model):
#     name = models.CharField(max_length= 50)
#     slug= models.SlugField(unique=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


class Genre(models.Model):
    name = models.CharField(max_length= 50)
    slug= models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# Choices = Categories.objects.all().values_list('name', 'name')

# choice_list= []

# for item in Choices:
#     choice_list.append(item)

class Album(models.Model):
    album_id=models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,blank=True, null=True)    
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='album_image', default='christ.png', blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    catalog = models.CharField(max_length=100, blank=True, null=True)
    beat_format = models.CharField(max_length=100, blank=True, null=True)
    descrip = RichTextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    # artist = models.CharField(max_length=100,blank=True, null=True)#, choices=choice_list)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'album'
        managed = True
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class Number_album(models.Model):
    created_albums = models.ForeignKey(Album, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_albums.name

class Beats(models.Model):
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null= True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,blank=True, null=True)
    beats_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug= models.SlugField(unique=True)
    subname = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    descrip = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='beat_image', default='christ.png', blank=True, null=True)
    beats = models.FileField(upload_to='beats_songs', blank=True, null=True)
    price= models.IntegerField(blank=True, null=True)
    display = models.BooleanField(blank=True, null=True)
    freedownload = models.BooleanField(blank=True, null=True)
    buy = models.BooleanField(blank=True, null=True)
    # artist = models.CharField(max_length=100,blank=True, null=True)#, choices=choice_list)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'beats'
        managed = True
        verbose_name = 'Beats'
        verbose_name_plural = 'Beats'

class Number_beat(models.Model):
    created_beats = models.ForeignKey(Beats, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_beats.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_beat = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album", null=True, blank=True)
    playsong_com = models.ForeignKey(Beats, on_delete = models.CASCADE, related_name= "listbeat", null=True, blank=True)
    name = models.CharField(max_length= 100,null=True, blank=True)
    pics = models.ImageField(default='christ.png')
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.comment_beat.name, self.user.username)