# # tweets/views.py
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView
# from django.urls import reverse
# from .models import Profile
#
# class ProfileListView(ListView):
#     model = Profile
#     template_name = 'PoliticianProfiles.html'
#
# class ProfileCreateView(CreateView):
#     model = Profile
#     template_name = 'profile_new.html'
#     fields = ['user', 'body']
#
#     def get_success_url(self):
#         return reverse('PoliticianProfiles')
