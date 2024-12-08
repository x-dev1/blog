from django.contrib import admin
from django.urls import path
from .views import index, about, post_detail, review_list

# Название приложения
app_name = 'posts'

# Урлы для приложения
urlpatterns = [
    path(
        '',
        index,
        name='index'
    ),
    path(
        'about/',
        about,
        name='about'
    ),
    path(
        '<int:post_id>/',
        post_detail,
        name='post'
    ),
    path(
        'reviews/',
        review_list,
        name='review_list'
    )
]