from django.core.mail import send_mail
from django.db import models
from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site

from .models import Ticket, Comment
from .forms import CommentForm


class TicketCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ticket
    fields = ('subject', 'body')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TicketListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    paginate_by = 3

    def get_queryset(self):
        queryset = super(TicketListView, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user)
        return queryset


class TicketOpenListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    paginate_by = 3

    def get_queryset(self):
        queryset = super(TicketOpenListView, self).get_queryset()
        queryset = queryset.filter(status='open', created_by=self.request.user)
        return queryset


class TicketClosedListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    paginate_by = 3

    def get_queryset(self):
        queryset = super(TicketClosedListView, self).get_queryset()
        queryset = queryset.filter(
            status='closed', created_by=self.request.user)
        return queryset


class TicketDetailView(LoginRequiredMixin, generic.edit.FormMixin, generic.DetailView):
    model = Ticket
    form_class = CommentForm

    def get_success_url(self):
        return reverse('ticket:ticket-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.ticket = self.object
        new_comment.save()
        self.send_email()
        return super().form_valid(form)

    def send_email(self):
        email_from = self.object.created_by.email
        send_mail(
            'Subject here',
            'Here is the message.',
            email_from,
            ['to@example.com'],
            fail_silently=False,
        )
        
        