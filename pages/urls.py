# pages/urls.py
from django.urls import path
from .views import MyInfoPageView, VotingReminderPageView, PollingLocationPageView

urlpatterns = [
    path('VotingReminder', VotingReminderPageView.as_view(), name='VotingReminder'),
    path('PollingLocation/', PollingLocationPageView.as_view(), name='PollingLocation'),
    path('', MyInfoPageView.as_view(), name='MyInfo'),
]
