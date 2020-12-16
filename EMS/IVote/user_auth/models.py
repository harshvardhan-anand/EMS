from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_candidate = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)    

    def __str__(self):
        return f'{self.user}'