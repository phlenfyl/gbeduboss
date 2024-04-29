from django.contrib import admin
from .models import *
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display=('first_word','second_word')
    list_display_links=('first_word','second_word')

admin.site.register(Banner, BannerAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display=('header_one','small_header','service_image')
    list_display_links=('header_one','small_header')

admin.site.register(Services, ServicesAdmin)


class SubnameAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_display_links=('name',)

admin.site.register(Subname, SubnameAdmin)


class SubdescriptionAdmin(admin.ModelAdmin):
    list_display=('owned_by','description','one','two','three','four','five','six')
    list_display_links=('description',)

admin.site.register(Subdescription, SubdescriptionAdmin)


class AdvertAdmin(admin.ModelAdmin):
    list_display=('third_header','third_subheader','link_name','link_one','link_nam','link_two','forth_header','forth_subheader')
    list_display_links=('third_header','forth_header')

admin.site.register(Advert, AdvertAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display=('name','subname','email')
    list_display_links=('name',)

admin.site.register(Newsletter, NewsletterAdmin)


admin.site.register(Booking)