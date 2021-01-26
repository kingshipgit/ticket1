from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Ticket, Comment
from .forms import CommentForm


class TicketListView(generic.ListView):
    model = Ticket
    paginate_by = 1

    def get_queryset(self, tag_slug=None, *args, **kwargs):
        queryset = Ticket.published.all()
        return queryset

    # def get_context_data(self, tag_slug=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class TicketDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Ticket
    form_class = CommentForm
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_success_url(self):
        return reverse('ticket:post_detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def get_context_data(self, tag_slug=None, **kwargs):
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
        return super().form_valid(form)
