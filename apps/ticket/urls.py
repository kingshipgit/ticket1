from django.urls import path

from . import views

app_name = 'ticket'

urlpatterns = [
    # ticket views
    path('', views.TicketListView.as_view(), name='ticket-list'),
    path('<int:pk>/<slug:slug>/',
         views.TicketDetailView.as_view(), name='post_detail'),
]
