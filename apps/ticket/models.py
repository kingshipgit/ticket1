from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from django.core.mail import send_mail


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

    def closed_ticket(self):
        return reverse('ticket:ticket-closed', args=[self.pk])

    def __str__(self):
        return self.subject


@receiver(post_save, sender=Ticket)
def ticket_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        ticket_url = '%s%s' % (Site.objects.get_current().domain,
                               instance.get_absolute_url())
        send_mail(
            'Subject here',
            ticket_url,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
    else:
        ticket_url = '%s%s' % (Site.objects.get_current().domain,
                               instance.get_absolute_url())
        send_mail(
            'Subject here',
            ticket_url,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )


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
