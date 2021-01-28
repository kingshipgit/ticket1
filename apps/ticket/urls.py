from django.urls import path

from . import views

app_name = 'ticket'

urlpatterns = [
    # ticket views
    path('', views.TicketListView.as_view(), name='ticket-list'),
    path('open/tickets/', views.TicketOpenListView.as_view(), name='ticket-open'),
    path('closed/tickets/', views.TicketClosedListView.as_view(), name='ticket-closed'),
    path('<int:pk>/',
         views.TicketDetailView.as_view(), name='ticket-detail'),
    path('create/', views.TicketCreateView.as_view(), name='ticket-create')
]
