from typing import Generic
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Profile
# from .forms import ProfileUpdateForm


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'ext')
    success_message = "Your profile has been modified"

    def test_func(self):
        return self.get_object().user == self.request.user

    
    def handle_no_permission(self):
        messages.warning(self.request, f'404 Error, object does not exist')
        return redirect('/')
