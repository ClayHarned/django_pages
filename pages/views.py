# pages/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'PoliticianProfiles.html'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile_new.html'
    fields = ['candidate', 'position', 'location', 'party', 'toppolicies']

    def get_success_url(self):
        return reverse('PoliticianProfiles')

    def get_login_url(self): # new
        return reverse('login') # new

    def form_valid(self, form): # new
        form.instance.user = self.request.user # new
        return super().form_valid(form) # new

class MyInfoPageView(TemplateView):
    template_name = 'MyInfo.html'

class VotingReminderPageView(TemplateView):
    template_name = 'VotingReminder.html'

class PollingInfoPageView(TemplateView):
    template_name = 'PollingInfo.html'

class VotingQuestionsAndTipsPageView(TemplateView):
    template_name = 'VotingQuestionsAndTips.html'
