from django.urls import path

from .views import ProfileUpdateView


app_name = 'accounts'

urlpatterns = [
    path('<slug:slug>/', ProfileUpdateView.as_view(), name='profile-update'),
]