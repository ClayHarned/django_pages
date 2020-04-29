# from django.db import models
#
# # Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    candidate = models.CharField(max_length=255, blank = False, default ='')
    position = models.CharField(max_length=255, blank = False)
    location = models.CharField(max_length=255, blank = False)
    party = models.CharField(max_length=255, blank = False)
    toppolicies = models.CharField(max_length=255, blank = False)



    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.candidate
        return self.position
        return self.location
        return self.party
        return self.TopPolicies
