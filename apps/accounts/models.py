from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(_('first_name'), max_length=200)
    last_name = models.CharField(_('last_name'), max_length=200, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    ext = models.CharField('extension', _("ext"), max_length=50, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('last_name',)
        index_together = (('id', 'slug'),)
        unique_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name, self.last_name)
        super().save(*args, **kwargs)

    @property
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def get_email(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('accounts:profile-update', kwargs={'slug': self.slug})

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name
        return self.user.username
