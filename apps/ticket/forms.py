from django import forms
from django.db.models import fields
from .models import Comment, Ticket


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
