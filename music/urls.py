from django.urls import path
from . import views



urlpatterns=[


    #music/14/
    path('<int:album_id>'+'/', views.details, name='details'),

    #music/14/favorite/
    path('<int:album_id>' + '/favorite/', views.favorite, name='favorite'),  #used for older favorite form
    # music/
    path('', views.index, name='index'),

]