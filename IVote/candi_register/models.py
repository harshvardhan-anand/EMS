from user_auth.models import Profile
from user_auth.models import Profile
from django.db import models
# Create your models here.
class Candidate(models.Model):
    DEP_CHOICE = (
        ('cs', 'CS'),
        ('it', 'IT'),
        ('ec', 'EC'),
        ('ee', 'EE'),
        ('me', 'ME'),
        ('ce', 'CE')
    )
    POSITION = (
        ('vp', 'Vice President'),
        ('general', 'General Secretary'),
        ('literary', 'Literary Secretary'),
        ('cultural', 'Cultural Secretary'),
        ('sports', 'Sports Secretary'),
        ('gmess', 'Girls Mess Secretary'),
        ('bmess', 'Boys Mess Secretary')
    )
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='candid')
    name = models.CharField(max_length=50)
    regno = models.IntegerField()
    idea = models.TextField(max_length=500)
    result = models.IntegerField(default=0)
    department = models.CharField(max_length=10, choices=DEP_CHOICE)
    position = models.CharField(max_length=100)
    year = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name