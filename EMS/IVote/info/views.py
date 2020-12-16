from django.shortcuts import render
from candi_register.models import Candidate

# Create your views here.
def show_candidate(request):
    candidate = Candidate.objects.filter(year__year=2020)
    print(candidate)
    return render(request, 'info/candidate.html')
