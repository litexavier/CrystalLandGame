import json
from django.shortcuts import render, render_to_response
from django.utils.html import strip_spaces_between_tags as short
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from models import GuildDB, MercenaryDB
import play_settings

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
    response = render_to_response('play/mercenaries_home.tpl', {'guild':guild}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

@login_required
def MercenariesMembers(request):
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '社团还未建立，不能雇佣', 'redirect': ''}))
    member_list = []
    for it in guild.mercenaries.all():
        member_list.append({'id': it.id, 'name': it.name, 'cls': play_settings.NEWPLAYER_CLASS_TABLE[it.cl]['name'], 'hp': it.maxhp, 'sp': it.maxsp, 'lv': it.lv, 'disp': it.dpf==0 })
    c = RequestContext(request, {'member_list': member_list})
    content = short(loader.get_template('play/mercenaries_members.tpl').render(c))
    return HttpResponse(json.dumps({'status': 'ok', 'msg': content}))

@login_required
def GetMemberDetail(request):
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '社团还未建立，不能雇佣', 'redirect': ''}))
    gid = request.GET.get('id', 0)
    print gid
    res=guild.mercenaries.filter(pk=gid)
    print res
    if len(res) <= 0:
        return HttpResponse(json.dumps({'status': 'fail', 'data': ''}))
    member_detail = {}
    member_detail['id'] = res[0].id
    member_detail['name'] = res[0].name
    member_detail['cls'] = play_settings.NEWPLAYER_CLASS_TABLE[res[0].cl]['name']
    member_detail['lv'] = res[0].lv
    member_detail['hp'] = res[0].maxhp
    member_detail['sp'] = res[0].maxsp
    member_detail['exp'] = res[0].exp
    member_detail['atk'] = res[0].atk
    member_detail['matk'] = res[0].matk
    member_detail['def'] = res[0]._def
    member_detail['mdef'] = res[0].mdef
    member_detail['speed'] =  res[0].spd
    member_detail['str'] = res[0]._str
    member_detail['vit'] = res[0]._vit
    member_detail['int'] = res[0]._int
    member_detail['apts'] = res[0].apts
    return HttpResponse(json.dumps({'status': 'ok', 'data': member_detail}))
        
@login_required
def DoCreateGuild(request):
    gd = GuildDB(id=request.user.id, name=request.POST.get("name", ""), gold=100, honor=0)
    try:
        gd.save(force_insert=True)
    except IntegrityError as e:
        if "column" in e:
            print e
            return HttpResponse(json.dumps({"status":"fail", "msg":"该社团已经存在"}))
        else:
            return HttpResponse(json.dumps({"status":"fail", "msg":"操作非法"}))
    return HttpResponse(json.dumps({"status":"ok", "msg":"创建社团成功","redirect": "/play/mercenaries"}))

@login_required
def Town(request):
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        response = render_to_response('play/mercenaries_new.tpl', {}, context_instance=RequestContext(request))
        if 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response
            
    response = render_to_response('play/town_home.tpl', {'guild':guild}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def Hire(request):
    item_list = []
    for it in play_settings.NEWPLAYER_CLASS_TABLE:
        pt = play_settings.NEWPLAYER_CLASS_TABLE[it]
        item_list.append({'id': it, 'classname':pt['name'], 'describe': pt['describe'], 'price': pt['price']})
    c = RequestContext(request, {'hire_item': item_list})
    content = short(loader.get_template('play/town_hire.tpl').render(c))
    return HttpResponse(json.dumps({'status': 'ok', 'msg': content}))

@login_required
def DoHire(request):
    cls = request.POST.get('clsname', '')
    if not cls in play_settings.NEWPLAYER_CLASS_TABLE:
        return HttpResponse(json.dumps({'status': 'fail', 'msg': '不能雇佣该级别的雇佣兵', 'redirect': ''}))
    pname = request.POST.get('pname', '')
    if pname == "":
        return HttpResponse(json.dumps({'status': 'fail', 'msg': '名字不能为空', 'redirect': ''}))
    try:
        guild = GuildDB.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '社团还未建立，不能雇佣', 'redirect': ''}))
    if len(guild.mercenaries.all()) >= play_settings.MAXMERCENARY_HIRED_PERGUILD:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '社团人数已达上限，不能雇佣', 'redirect': ''}))
    for i in guild.mercenaries.all() :
        if pname == i.name :
            return HttpResponse(json.dumps({'status':'fail', 'msg': '社团里已有人起该名字', 'redirect': ''}))
    tab = play_settings.NEWPLAYER_CLASS_TABLE[cls]
    pr  = int(tab['price'])
    if guild.gold < pr:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '社团资金不足，无法雇佣', 'redirect': ''}))
    mec = MercenaryDB(name = pname, cl= cls, maxhp = tab['hp'], maxsp = tab['sp'], atk=tab['atk'], matk=tab['matk'], _def=tab['def'], mdef=tab['mdef'], spd=tab['spd'], _str= 1, _vit= 1, _int= 1)
    try:
        mec.save()
        guild.mercenaries.add(mec)
        guild.gold -= pr
        guild.save()
    except Expection as e:
        return HttpResponse(json.dumps({'status':'fail', 'msg': '系统异常', 'redirect': ''}))
    return HttpResponse(json.dumps({'status': 'ok', "msg":"雇佣成功", "redirect": "/play/mercenaries/"}))
