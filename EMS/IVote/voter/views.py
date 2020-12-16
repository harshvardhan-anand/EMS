from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from .models import ElectionStatus
from common.decorator import election_is_active
from candi_register.models import Candidate
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = None
    request.session['user_is_active'] = 1     
    return render(request, 'voter/index.html', context)

@election_is_active # we will see this vote page only if we have any active elction
@login_required # user can see this view only if he is logged in 
def vote(request):
    tab_context = {
        'show_tab':True,
        'show_candidate':False
    }
    try:
        if request.session['user_is_active']:
            pass
    except:
        return HttpResponseRedirect(reverse('voter:homepage'))
    if request.session['user_is_active']:
        # if user hasn't voted till now
        candi = Candidate.objects.all()
        candidate = {}
        POSITION = {
                'Vice President',
                'General Secretary',
                'Literary Secretary',
                'Cultural Secretary',
                'Sports Secretary',
                'Girls Mess Secretary',
                'Boys Mess Secretary'
            }           
        try:
            if ElectionStatus.objects.all()[0].poll_started:
                tab_context = {
                    'show_tab' : False,
                    'show_candidate':True
                }                          
        except:
            pass              
        for position in POSITION:
            candidate[position] = candi.filter(position=position)
        context = {'show_result_tab':False, 'all_candidates':candidate, 'register_input':True} #list of all candidate
    else: #if user has voted
        context = {'response':'Thank You For Your Vote', 'show_result_tab':False, 'register_input':False}
    return render(request, 'voter/vote.html', {**context, **tab_context})

@login_required
@election_is_active
def voted(request):
    user = User.objects.get(username=request.user)
    user.is_active=False
    messages.success(request, 'Thank You For Your Vote')
    user.save()
    request.session['user_is_active'] = 0
    cd = request.POST
    print(cd)
    POSITION = [
            'Vice President',
            'General Secretary',
            'Literary Secretary',
            'Cultural Secretary',
            'Sports Secretary',
            'Girls Mess Secretary',
            'Boys Mess Secretary'
        ]
    for name in POSITION:
        try:
            opted_candidate = Candidate.objects.get(regno=cd[name])  
            opted_candidate.result += 1
            opted_candidate.save()
        except:
            pass
    return HttpResponseRedirect(reverse('voter:homepage'))