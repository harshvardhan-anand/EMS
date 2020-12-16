from django.shortcuts import render
# from .forms import RegisterCandidate
from user_auth.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Candidate
# Create your views here.
@login_required
def candidate_register(request):
    if request.method == 'POST':
        print(request.POST)
        profile = Profile.objects.get(user=request.user)
        if profile.is_candidate == False:
            profile.is_candidate = True
            profile.save()
            cd = request.POST
            new_candidate = Candidate()
            new_candidate.user_profile = profile
            new_candidate.name = cd['textnames']
            new_candidate.regno = cd['regno']
            new_candidate.department = cd['dept']
            new_candidate.position = cd['position']
            new_candidate.idea = cd['feedback']
            print(new_candidate)
            new_candidate.save()
                # after registering send them to vote page
            messages.success(request, "You have registered yourself in the election")
            return HttpResponseRedirect(reverse('voter:vote'))  
        # if already registered then create message "you have already registered"
        else:       
            messages.error(request, 'You have already registered!!')
            return HttpResponseRedirect(reverse('candi_register:register'))

    return render(request, 'candi_register/registerpg.html')