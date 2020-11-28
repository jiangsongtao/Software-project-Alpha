from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from  imgupload import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径