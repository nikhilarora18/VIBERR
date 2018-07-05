
from django.contrib import admin
from django.urls import path,include,re_path
#from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/',include('music.urls')),
    path('', include('music.urls')),

]
