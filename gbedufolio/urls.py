from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.views.static import serve



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('gbeduboss.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("convert/", include("guest_user.urls")),
    path("paypal/", include("paypal.standard.ipn.urls")),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)