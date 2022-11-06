from django.contrib import admin
from django.urls import path, include
from . import views

# for image 
from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('App_Blog.urls')),
    path('account/', include('App_Login.urls')),
    path('', views.Index, name='index')
]


# image
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)