from django.urls import path

from .views import contact, blog_list, post_detail


urlpatterns = [
    path('', blog_list, name='blog_posts'),
    path('contact/', contact, name='blog_contact'),
    path('<slug:post_slug>/', post_detail, name='blog_post')
]
