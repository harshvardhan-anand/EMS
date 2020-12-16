from .models import Candidate
from django import forms

class RegisterCandidate(forms.ModelForm):
    Email_ID = forms.EmailField()
    Date_of_Birth = forms.DateField()
    CGPA = forms.FloatField(required=False)
    Current_Position = forms.CharField(max_length=50, label='Current Position(If any)')
    class Meta:
        model = Candidate
        fields = ('name', 'regno', 'idea', 'department', 'position')