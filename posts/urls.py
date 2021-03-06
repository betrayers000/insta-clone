from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('hashtags/<int:id>/', views.hashtags, name="hashtag"),
    path('like/<int:id>/', views.like, name="like"),
    path('<int:id>/update', views.update, name="update")
]
