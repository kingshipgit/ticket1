from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('complete', 'Complete'),
        ('waiting for part', 'Waiting for part'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='created')

    class Meta:
        ordering = ('-publish',)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('ticket:post_detail', args=[self.pk, self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,
                             on_delete=models.CASCADE, related_name='comments')
    # email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.ticket}'
