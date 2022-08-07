from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('createalbum/', views.album, name = 'create-album'),
    path('addphoto/', views.addphoto, name = 'add-photo'),
    path('soloalbum/<int:id>', views.soloalbum, name = 'soloalbum')
]