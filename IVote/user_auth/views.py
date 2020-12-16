from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        request.session['user_is_active'] = 1
        # form = Login(request.POST)
        cd = request.POST
        # print(cd)
        # if form.is_valid():
        user = authenticate(request, username=cd['Uname'], password=cd['Pass'])
        print(user)
        if user is not None: # If user exist with given username and password
            if user.is_active: # if user has not given his/her vote
                auth_login(request, user)
                try:
                    user = Profile.objects.get(user=user)
                except:
                    return HttpResponse('<h1>You are Unauthorised</h1>')
                if user.is_admin:
                    return HttpResponseRedirect(reverse('show_admin:admin'))
                elif user.is_candidate:
                    return HttpResponseRedirect(reverse('voter:vote'))
                if user.is_voter:
                    return HttpResponseRedirect(reverse('voter:vote'))
            else: # if user has given his/her vote
                auth_login(request, user)
                request.session['user_is_active'] = 0
                return HttpResponseRedirect(reverse('voter:vote'))
        else: # if user is not in the database
            messages.error(request, 'Either you have casted your vote or you are not authorized to login.')
            return HttpResponseRedirect(reverse('voter:homepage'))
    else:
        return render(request, 'user_auth/loginpage.html')

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('voter:homepage'))