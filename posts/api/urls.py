from django.urls import path
from .views import personPosts, newPost, postOperations, getPosts

urlpatterns = [
    path('api/person/<int:pk>/posts/', personPosts), # if we have a person id
    path('api/person/posts', getPosts), # posts of logged in user
    path('api/post/new', newPost),
    path('api/post/<int:pk>', postOperations), # get, need auth any TODO: friend # put, need auth any # post, need auth author # delete, need auth author
]