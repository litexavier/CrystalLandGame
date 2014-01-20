from django.shortcuts import render, render_to_response
from battleengine import BattleEngine
import actmode, skills
from char import Monster
from django.utils.html import strip_spaces_between_tags as short
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import DungeonDB, MonsterDB
from dungeon import Dungeon
import json

# Create your views here.
def testbattle(request, teamid1, teamid2):
    team1 = Dungeon().load(int(teamid1)).generateTeam()
    team2 = Dungeon().load(int(teamid2)).generateTeam()
    # AI
    be = BattleEngine(maxturn=200, action_spd=100)
    rec = be.battle(team1, team2)
    response = render_to_response('battlelog.tpl', {'log':rec})
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def showdungeon(request):
    dungeon_infos = []
    for i in DungeonDB.objects.all():
        dun = {}
        dun["id"] = i.id
        dun["name"] = i.name
        dun["monsters"] = ""
        dungeon_infos.append(dun)
        dun["resetby"] = i.resetbybattle
    response = render_to_response('dungeonshow.tpl', {"dlist":dungeon_infos}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def adddungeon(request):
    d = Dungeon()
    d.name = request.POST[u'dname']
    if 'yes' in request.POST[u'rbb']:
        d.resetbybattle = 1
    else:
        d.resetbybattle = 0
    d.save()
    return HttpResponseRedirect("/dungeon/show/")

def deldungeon(request, did):
    DungeonDB.objects.get(id=did).delete()
    return HttpResponseRedirect("/dungeon/show/")

def moddungeon(request, did):
    d = Dungeon()
    d.load(did)
    monster_infos = []
    for i in MonsterDB.objects.all():
        mon = {}
        mon["id"] = "%d" % i.mid
        mon["name"] = i.name
        monster_infos.append(mon)
    ailist = []
    for i in actmode.actionmodelist:
        ai = {}
        ai["id"] = "%d" % i.id
        ai["name"] = i.name
        ailist.append(ai)
    skill_list = []
    for i in skills.skilllist:
        sk = {}
        sk["id"] = "%d" % i.id
        sk["name"] = i.name
        skill_list.append(sk)
    response = render_to_response('dungeonmod.tpl', {"did":did, "name":d.name, "minfo":monster_infos, "ailist":ailist, "sk":skill_list, "data":d.data}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def addmonster(request):
    d = Dungeon()
    d.load(int(request.POST["did"]))
    d.addmon(request.POST["data"])
    d.save()
    monster_infos = []
    for i in MonsterDB.objects.all():
        mon = {}
        mon["id"] = "%d" % i.mid
        mon["name"] = i.name
        monster_infos.append(mon)
    ailist = []
    for i in actmode.actionmodelist:
        ai = {}
        ai["id"] = "%d" % i.id
        ai["name"] = i.name
        ailist.append(ai)
    skill_list = []
    for i in skills.skilllist:
        sk = {}
        sk["id"] = "%d" % i.id
        sk["name"] = i.name
        skill_list.append(sk)
    response = render_to_response('dungeonmod_basic.tpl', {"did":request.POST["did"], "name":d.name, "minfo":monster_infos, "ailist":ailist, "sk":skill_list, "data":d.data}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def delmonster(request):
    d = Dungeon()
    d.load(int(request.POST["did"]))
    d.delmon(int(request.POST["mid"])-1)
    d.save()
    monster_infos = []
    for i in MonsterDB.objects.all():
        mon = {}
        mon["id"] = "%d" % i.mid
        mon["name"] = i.name
        monster_infos.append(mon)
    ailist = []
    for i in actmode.actionmodelist:
        ai = {}
        ai["id"] = "%d" % i.id
        ai["name"] = i.name
        ailist.append(ai)
    skill_list = []
    for i in skills.skilllist:
        sk = {}
        sk["id"] = "%d" % i.id
        sk["name"] = i.name
        skill_list.append(sk)
    response = render_to_response('dungeonmod_basic.tpl', {"did":request.POST["did"], "name":d.name, "minfo":monster_infos, "ailist":ailist, "sk":skill_list, "data":d.data}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response

def modmonster(request):
    d = Dungeon()
    d.load(int(request.POST["did"]))
    d.modmon(int(request.POST["mid"])-1, request.POST["data"])
    d.save()
    monster_infos = []
    for i in MonsterDB.objects.all():
        mon = {}
        mon["id"] = "%d" % i.mid
        mon["name"] = i.name
        monster_infos.append(mon)
    ailist = []
    for i in actmode.actionmodelist:
        ai = {}
        ai["id"] = "%d" % i.id
        ai["name"] = i.name
        ailist.append(ai)
    skill_list = []
    for i in skills.skilllist:
        sk = {}
        sk["id"] = "%d" % i.id
        sk["name"] = i.name
        skill_list.append(sk)
    response = render_to_response('dungeonmod_basic.tpl', {"did":request.POST["did"], "name":d.name, "minfo":monster_infos, "ailist":ailist, "sk":skill_list, "data":d.data}, context_instance=RequestContext(request))
    if 'text/html' in response['Content-Type']:
        response.content = short(response.content)
    return response
    
