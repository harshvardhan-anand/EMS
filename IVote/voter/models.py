from django.db import models

# Create your models here.
class ElectionStatus(models.Model):
    election_start = models.DateField(auto_now=False, auto_now_add=True)
    election_end = models.DateField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    poll_started = models.BooleanField(default=False)
    result_declared = models.BooleanField(default=False)

    class Meta:
        ordering = ('-election_start',)

    def __str__(self):
        return f'{str((self.election_start).year)}-{str((self.election_start).month)}'