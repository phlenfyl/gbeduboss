from django.urls import path
from django.views.static import serve
from django.conf import settings
from . import views



urlpatterns=[
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.musiclist, name='categories_by_category'),
    path('genre/<slug:genre_slug>', views.musiclist, name='genres_by_genre'),
    path('tag/<slug:tag_slug>', views.musiclist, name='beat_by_tag'),
    path('tag/<slug:tag_slug>', views.musiclist, name='album_by_tag'),
    path('musiclist', views.musiclist, name='musiclist'),
    path('download/<str:id>/', views.download, name= 'download'),

    path('playsong/<str:id>/<str:slug>', views.playsong, name='playsong'),
    path('remove_beat_comment/<str:id>/<str:slug>', views.remove_beat_comment, name='remove_beat_comment'),
    path('albumsong/<str:id>/<str:slug>', views.albumsong, name='albumsong'),
    path('remove_album_comment/<str:id>/<str:slug>', views.remove_album_comment, name='remove_album_comment'),
    path('booking', views.booking, name='booking'),
    # path('tag/<slug:tag_slug>', views.albumsong, name='album_by_tag'),

    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('loggout', views.loggout, name='loggout'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('checkout', views.checkout, name='checkout'),
    path('paidorder', views.paidorder, name='paidorder'),
    path('cback', views.cback, name='cback'),
    path('cancel', views.cancel, name='cancel'),
    path('thankyou', views.thankyou, name='thankyou'),
]