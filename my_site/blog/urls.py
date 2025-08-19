from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index-page'),
    path('posts', views.posts, name='posts-page'),  # /posts
    path('posts/<slug:post_slug>', views.post_detail, name='post-detail-page'),   # /posts/<post_title>
]
