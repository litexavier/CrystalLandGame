# -*- coding: utf-8 -*-

def info_extract(team, fr, bk):
    for ch in team:
        if ch.pos == 0:
            fr.append({"name":ch.name, "hp":ch.hp, "maxhp":ch.maxhp, "sp":ch.sp, "maxsp":ch.maxsp, "spdb":ch.spd_bar})
        else:
            bk.append({"name":ch.name, "hp":ch.hp, "maxhp":ch.maxhp, "sp":ch.sp, "maxsp":ch.maxsp, "spdb":ch.spd_bar})                

class BattleRecorder(object):
    def __init__ (self):
        self.rec = []
        self.side = 1
        self.cri = False
        
    def add(self, it):
        self.rec.append(it)
        
    def set_team_flag(self, tf):
        self.side = tf

    def useskill(self, name, skillname):
        self.add({"type":1, "s":self.side, "name":name, "skill":skillname})

    def failuseskill(self, name):
        self.add({"type":4, "s":self.side, "name":name})
        
    def damaged(self, name, dam, prot_per, is_cri):
        self.add({"type":2, "s":self.side, "name":name, "dam":dam, "pro":prot_per, "cri":is_cri})

    def dead(self, name):
        self.add({"type":3, "s":self.side, "name":name})
    
    def tied(self):
        self.add({"type":0, "msg": "平局!".decode('utf-8')})

    def t1win(self):
        self.add({"type":0, "msg": "Team1 赢了".decode('utf-8')})

    def t2win(self):
        self.add({"type":0, "msg": "Team2 赢了".decode('utf-8')})

    def charging(self, name, barbe, baraf):
        self.add({"type":5, "s":self.side, "name":name, "barbe":barbe, "baraf":baraf})

    def casting(self, name, barbe, baraf):
        self.add({"type":6, "s":self.side, "name":name, "barbe":barbe, "baraf":baraf})

    def stat_attach(self, name, statname):
        self.add({"type":7, "s":self.side, "name":name, "statname":statname})

    def stat_run(self, statname, name, dmg):
        self.add({"type":8, "s":self.side, "name":name, "statname":statname, "dmg":dmg})
        
    def broadcast(self, turn, team1, dteam1, team2, dteam2):
        t1fr = []
        t1bk = []
        info_extract(team1, t1fr, t1bk)
        info_extract(dteam1, t1fr, t1bk)
        t2fr = []
        t2bk = []
        info_extract(team2, t2fr, t2bk)
        info_extract(dteam2, t2fr, t2bk)         
        self.add({"type":4, "turn": turn-1, "t1fr":t1fr, "t1bk":t1bk, "t2fr":t2fr, "t2bk":t2bk})
