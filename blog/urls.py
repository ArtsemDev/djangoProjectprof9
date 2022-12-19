from django.urls import path

from .views import about, contact, PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='blog_posts'),
    path('contact/', contact, name='blog_contact'),
    path('about/', about, name='blog_about'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='blog_post')
]
