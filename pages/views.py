# pages/views.py
from django.views.generic import TemplateView

class MyInfoPageView(TemplateView):
    template_name = 'MyInfo.html'

class VotingReminderPageView(TemplateView):
    template_name = 'VotingReminder.html'

class PollingLocationPageView(TemplateView):
    template_name = 'PollingLocation.html'
