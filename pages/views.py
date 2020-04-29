# pages/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'PoliticianProfiles.html'

class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile_new.html'
    fields = ['candidate', 'position', 'location', 'party', 'toppolicies', 'user']

    def get_success_url(self):
        return reverse('PoliticianProfiles')

class MyInfoPageView(TemplateView):
    template_name = 'MyInfo.html'

class VotingReminderPageView(TemplateView):
    template_name = 'VotingReminder.html'

class PollingInfoPageView(TemplateView):
    template_name = 'PollingInfo.html'

class VotingQuestionsAndTipsPageView(TemplateView):
    template_name = 'VotingQuestionsAndTips.html'
