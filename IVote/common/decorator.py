from django.urls import reverse
from voter.models import ElectionStatus
from django.http import HttpResponseRedirect
from django.contrib import messages

# if election is not active then say "No active election"
def election_is_active(f):
    def wrap(request, *args, **kwargs):
        try:
            if ElectionStatus.objects.all()[0].is_active == False:
                messages.error(request, 'No Active Election')
                return HttpResponseRedirect(reverse('voter:homepage'))
        except:
            pass
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

def result_declared(f):
    def wrap(request, *args, **kwargs):
        try:
            # If election is active and result is not declared then say "Result Not declared"
            if ElectionStatus.objects.all()[0].result_declared==False:
                messages.error(request, 'Result is not declared')
                return HttpResponseRedirect(reverse('voter:homepage'))
        except:
            pass
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap 
