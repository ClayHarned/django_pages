# pages/urls.py
from django.urls import path
from .views import MyInfoPageView, PoliticianProfilesPageView, PollingLocationPageView, VotingReminderPageView, VotingQuestionsAndTipsPageView

urlpatterns = [
    path('VotingQuestionsAndTips/', VotingQuestionsAndTipsPageView.as_view(), name='VotingQuestionsAndTips'),
    path('VotingReminder/', VotingReminderPageView.as_view(), name='VotingReminder'),
    path('PollingLocation/', PollingLocationPageView.as_view(), name='PollingLocation'),
    path('PoliticianProfiles/', PoliticianProfilesPageView.as_view(), name='PoliticianProfiles'),
    path('', MyInfoPageView.as_view(), name='MyInfo')

]
