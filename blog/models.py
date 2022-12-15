from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='название',
        help_text='Макс. 64 символа'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'blog_categories'


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='заголовок'
    )
    descr = models.TextField(verbose_name='описание')
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='дата создания'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='категория'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'post_slug': self.slug})

    @property
    def date(self) -> str:
        return self.date_created.strftime('%d.%m.%y')

    @property
    def full_name(self):
        return self.author.first_name + ' ' + self.author.last_name

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['date_created']


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя')
    email = models.EmailField(verbose_name='почта')
    message = models.CharField(max_length=1024, verbose_name='сообщение')
    date_created = models.DateTimeField(default=now, verbose_name='дата обращения')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_contacts'
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['date_created']
