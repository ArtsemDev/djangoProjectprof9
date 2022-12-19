from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import ContactForm
from .models import Post, Contact


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
        context['form'] = ContactForm()
        context.update(self.context)
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class AboutTemplateView(BaseMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'about us'
        context['coordinate'] = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10221.793301433216!2d27.54570734394003!3d53.906860922347065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46dbcf94b327141f%3A0xd74e660de1f79fe9!2z0J3QtdC80LjQs9Cw!5e1!3m2!1sru!2sby!4v1671128718358!5m2!1sru!2sby'
        context['about'] = '''
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
ABOUT ABOUT ABOUT ABOUT        
'''
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'blog/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('blog_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'CONTACT'
        return context


def error404(request, exception):
    return render(request, 'blog/error404.html')
