# tweets/urls.py
from django.urls import path
from .views import ProfileListView, ProfileCreateView

urlpatterns = [
    path('profiles/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('', ProfileListView.as_view(), name='home'),
]
