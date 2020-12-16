from common.decorator import result_declared
from common.decorator import election_is_active
from candi_register.models import Candidate
import os
from user_auth.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from voter.models import ElectionStatus
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import pandas as pd
import random
import numpy as np
import string
from django.core.mail import send_mail

# Create your views here.
# registration time
@login_required
def admin(request):
    try:
        if ElectionStatus.objects.all()[0].is_active:
            if ElectionStatus.objects.all()[0].poll_started==False:
                if ElectionStatus.objects.all()[0].result_declared==False:
                    # registration time
                    # as election=true, poll=false, result = false
                    # button - start poll
                    status = 'registration-time'
                else:
                    # as election=true, poll=false, result = true
                    # button - stop election
                    status = 'stop-election'
            else:
                # as election=true, poll=true, result = false
                # button - stop polling
                status='polling'
        else:
            # as election=false, poll=false, result = false
            # button - start election
            status='no-active-election'
    except:
        # This will be executed only once
        status='no-active-election'
    try:
        if request.session['message_count']:
            message = request.session['message']
            message_kind = request.session['message_kind']
            request.session['message_count'] = 0
        else:
            message = None
            message_kind = None
    except:
        message = None
        message_kind = None
    return render(request, 'show_admin/admin.html', {'status':status, 'message':message, 'message_kind': message_kind})

@login_required
def operation(request):
    try:
        failed_email = []
        data = request.POST
        np.random.seed = 347
        # creating 15 character long strong password
        create_password = lambda:''.join([random.choice(string.ascii_letters) for i in range(5)]+[random.choice(string.digits) for i in range(5)]+[random.choice(string.punctuation) for i in range(5)])
        stud_path = os.path.join(os.path.dirname('__file__'), 'show_admin', 'user_list', 'students.csv')
        # starting election and checking for any new emails to add it to database
        if data['next']=='Start Election':
            students = pd.read_csv(stud_path).email
            for studemail in students:
                try:
                    user = User.objects.create_user(username=studemail, password=create_password())
                    user.save()
                except Exception as E:
                    print(E)
                try:
                    profile = Profile(user=User.objects.get(username=studemail))
                    print(profile.user)
                    profile.is_voter = True
                    profile.save()
                except Exception as e:
                    print(e)
        try:
            election = ElectionStatus.objects.all()[0]
        except:
            # If election is carried for the first time
            election = ElectionStatus()
        if data['next']=='Start Election':
            # reading emails from csv
            students = pd.read_csv(stud_path).email
            for studemail in students:
                user = User.objects.get(username=studemail)
                user.is_active = True
                pasw = create_password()
                user.set_password(pasw)
                user.save()
                try:
                    send_mail(
                        'Credentials For Upcoming Election',
                        f'Username: {studemail}\nPassword:{pasw}\nDo not share this credentials with anyone in any case.',
                        'SMIT ELECTION SERVICES',
                        [studemail],
                        fail_silently=False,
                    )
                except:
                    failed_email.append(studemail)
                failed = np.array(failed_email)
                np.savetxt("failed.csv", failed, delimiter = ",")   
            if (len(failed_email))==0:
                election.is_active = True
                election.poll_started = False
                election.result_declared = False
                election.save()
                request.session['message'] = "Login Id and Password for Election has been sent to your email"
                request.session['message_kind'] = "success"
                request.session['message_count'] = 1
            else: 
                request.session['message'] = "Election is not started as all the students have not recieved the email"
                request.session['message_kind'] = "error"
                request.session['message_count'] = 1
                return HttpResponseRedirect(reverse('show_admin:admin'))
    except:
        request.session['message'] = "Email Server not configured."
        request.session['message_kind'] = "error"
        request.session['message_count'] = 1
        return HttpResponseRedirect(reverse('show_admin:admin'))
    if data['next']=='Start Polling':
        election.poll_started = True
        election.save()
    if data['next']=='Stop Polling':
        election.poll_started = False
        election.result_declared = True
        election.save()
        return HttpResponseRedirect(reverse('show_admin:result'))
    if data['next']=='Stop Election':
        election.is_active = False
        election.save()
        candidates = Candidate.objects.all()
        for candidate in candidates:
            candidate.result = 0
            candidate.save()
    return HttpResponseRedirect(reverse('show_admin:admin'))

@election_is_active
@result_declared
def result(request):
    candi = Candidate.objects.all()
    result = {}
    POSITION = {
            'Vice President',
            'General Secretary',
            'Literary Secretary',
            'Cultural Secretary',
            'Sports Secretary',
            'Girls Mess Secretary',
            'Boys Mess Secretary'
        }
    
    for position in POSITION:
        try:
            result[position] = candi.filter(position=position).order_by('-result')[0]
        except:
            pass
    return render(request, 'show_admin/result.html', {'result':result})
        
        