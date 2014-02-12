from django.shortcuts import render, render_to_response
from django.utils.html import strip_spaces_between_tags as short
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def Main(request):
    response = render_to_response('play/play_index.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def Register(request):
    response = render_to_response('play/play_register.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def DoRegister(request):
    username = request.POST.get('UserName', '')
    password = request.POST.get('Password', '')
    user = User.objects.create_user(username=username, password=password)
    user.save()
    auth_user = auth.authenticate(username=username, password=password)
    auth_user.login(request, user)
    return HttpResponseRedirect("/play/")

def LoginPage(request):
    response = render_to_response('play/play_login.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def DoLogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/play/")

@login_required
def DoLogout(request):
    auth.logout(request)
    return HttpResponseRedirect("/play/")
