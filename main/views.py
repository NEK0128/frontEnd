from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
def index(request):
    return render_to_response('index.html',{ 'user':request.user })

def logout_process(request):
    logout(request)
    return HttpResponseRedirect('/main')


def logged_in(request):
	return render_to_response('logged_in.html', {
	}, context_instance=RequestContext(request))
