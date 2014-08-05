import json
from django.shortcuts import render, render_to_response
from django.utils.html import strip_spaces_between_tags as short
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from models import GuildDB

# Create your views here.
def Main(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/play/mercenaries/")

    response = render_to_response('play/play_index.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def Register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/play/mercenaries/")

    response = render_to_response('play/play_register.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def DoRegister(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({"status":"fail", "msg":"您已经登录", "redirect": "/play/"}))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
    except IntegrityError:
        return HttpResponse(json.dumps({"status":"fail", "msg":"用户名已存在", "redirect": ""})) 
    except:
        return HttpResponse(json.dumps({"stauts":"fail", "msg":"未知错误", "redirect": ""}))
        auth_user = auth.authenticate(username=username, password=password)
        auth.login(request, auth_user)
    return HttpResponse(json.dumps({"status":"ok", "msg":"注册成功", "redirect": "/play/mercenaries"}))

def LoginPage(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/play/mercenaries/")

    response = render_to_response('play/play_login.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def DoLogin(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({"status":"fail", "msg":"您已经登录", "redirect": "/play/"}))

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    else:
        return HttpResponse(json.dumps({"status":"fail","msg":"用户名密码错误", "redirect": ""}))
    
    return HttpResponse(json.dumps({"status":"ok","msg":"","redirect":"/play/mercenaries"}))

@login_required
def DoLogout(request):
    auth.logout(request)
    return HttpResponseRedirect("/play/")

@login_required
def Mercenaries(request):
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        response = render_to_response('play/mercenaries_new.tpl', {}, context_instance=RequestContext(request))
        if 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response
            
    response = render_to_response('play/mercenaries_home.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response
        
@login_required
def DoCreateGuild(request):
    gd = GuildDB(id=request.user.id, name=request.GET.get("name", ""), gold=0, honor=0)
    try:
        gd.save(force_insert=True)
    except IntegrityError as e:
        if "column" in e.message:
            return HttpResponse(json.dumps({"status":"fail", "msg":"该社团已经存在"}))
        else:
            return HttpResponse(json.dumps({"status":"fail", "msg":"操作非法"}))
    return HttpResponse(json.dumps({"status":"ok", "msg":""}))

@login_required
def Town(request):
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        response = render_to_response('play/mercenaries_new.tpl', {}, context_instance=RequestContext(request))
        if 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response
            
    response = render_to_response('play/town_home.tpl', {}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

@login_required
def DoHire(request):
    print request.POST
    return HttpResponse(json.dumps({"flag":"succ", "msg":""}))
