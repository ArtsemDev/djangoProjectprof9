from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Post
from .forms import ContactForm


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'github': 'https://github.com',
    }


class PostListView(BaseMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'MIXIN HEADING'
        context['subheading'] = 'mixin subheading'
        context.update(self.context)
        return context


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


# @require_GET
# def blog_list(request: HttpRequest):
#     posts_list = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts': posts_list})


# def post_detail(request: HttpRequest, post_slug: str):
#     post = get_object_or_404(Post, slug=post_slug)
#     return render(request, 'blog/post.html', {'post': post})


def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'blog/contact.html', {'contact_form': form})


def about(request: HttpRequest):
    return render(request, 'blog/about.html')


def error404(request, exception):
    return render(request, 'blog/error404.html')
