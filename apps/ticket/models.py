from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('closed', 'Closed'),
        ('resolved', 'Resolved'),
    )
    subject = models.CharField(max_length=250)
    created_by = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='open')

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('ticket:ticket-detail', args=[self.pk])

    def __str__(self):
        return self.subject


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE, related_name='comments')
    # email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.comment} on {self.ticket}'
