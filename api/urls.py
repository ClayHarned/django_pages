# api/urls.py
from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('pages/', ProfileList.as_view()),
    path('pages/<int:pk>/', ProfileDetail.as_view()),
]
