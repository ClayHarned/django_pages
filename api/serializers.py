# api/serializers.py
from rest_framework import serializers
from pages.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'candidate', 'position', 'location', 'party', 'toppolicies', 'created_at', 'updated_at']
