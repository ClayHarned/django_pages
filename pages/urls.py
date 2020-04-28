# pages/urls.py
from django.urls import path
from .views import ProfileListView, ProfileCreateView, MyInfoPageView, PollingInfoPageView, VotingReminderPageView, VotingQuestionsAndTipsPageView

urlpatterns = [
    path('VotingQuestionsAndTips/', VotingQuestionsAndTipsPageView.as_view(), name='VotingQuestionsAndTips'),
    path('VotingReminder/', VotingReminderPageView.as_view(), name='VotingReminder'),
    path('PollingInfo/', PollingInfoPageView.as_view(), name='PollingInfo'),
    path('profiles/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('PoliticianProfiles/', ProfileListView.as_view(), name='PoliticianProfiles'),
    path('', MyInfoPageView.as_view(), name='MyInfo')

]
