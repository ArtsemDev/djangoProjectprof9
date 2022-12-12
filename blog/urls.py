from django.urls import path

from .views import blog_list, post_detail


urlpatterns = [
    path('', blog_list, name='blog_posts'),
    path('<slug:post_slug>/', post_detail, name='blog_post')
]
