from logrec import BattleRecorder
from gameutils import random_pick

def move_dead_char(team, dead_team, logrec):
    moved_team = []
    for ch in team:
        if ch.hp == 0:
            ch.alive = False
            logrec.dead(ch.name)
        if not ch.alive:
            dead_team.append(ch)
        else:
            moved_team.append(ch)
    return moved_team

def get_min_time(target, team):
    res = target
    for ch in team:
        t = ( target - ch.spd_bar + ch.spd - 1 ) / ch.spd
        if res > t:
            res = t
    return res

class BattleTeam(object):
    def __init__(self, name, team, side):
        self.name = name
        self.team = team
        self.side = side
        self.dead = []
        for i in self.team:
            i.team_flag = side
            i.team_obj  = self

    def reset_time_bar(self):
        for i in self.team:
            i.spd_bar = 0

    def set_all_alive(self):
        for i in self.team:
            i.alive = True

    def move_all_dead(self, logrec):
        new_team = []
        for i in self.team:
            if i.hp <= 0:
                i.alive = False
                logrec.dead(i.name)
            if i.alive:
                new_team.append(i)
            else:
                self.dead.append(i)
        self.team = new_team

def skill_applied(skill, tiggered_char, friends, enemies, recorder):
    if not skill.cost.do(tiggered_char):
        recorder.failuseskill(tiggered_char.name)
        return False
    recorder.useskill(tiggered_char.name, skill.name)
    for i in range(0, skill.times):
        target = skill.selector.do(tiggered_char, friends.team, enemies.team)
        skill.applied(tiggered_char, target, recorder)
        if target.hp <= 0:
            target.team_obj.move_all_dead(recorder)
    return True

class BattleEngine(object):
    def __init__ (self, maxturn, action_spd):
        self.maxturn = maxturn
        self.action_spd = action_spd
        self.broadcastturn = 10
        
    def battle(self, team1, team2):
        recorder = BattleRecorder () # create a new battle recorder
        # start battle
        turn = 1
        team1 = BattleTeam("Team1", team1, 1)
        team2 = BattleTeam("Team2", team2, 2)
        team1.reset_time_bar()
        team2.reset_time_bar()
        team1.set_all_alive()
        team2.set_all_alive()
        team1.move_all_dead(recorder)
        team2.move_all_dead(recorder)
        while turn <= self.maxturn:
            al1 = len(team1.team)
            al2 = len(team2.team)
            if al1 == 0 and al2 == 0:
                recorder.tied()
                break
            elif al2 == 0:
                recorder.t1win()
                break
            elif al1 == 0:
                recorder.t2win()
                break
            if turn % self.broadcastturn == 1: # Need broadcast
                recorder.broadcast(turn, team1.team, team1.dead, team2.team, team2.dead)
            # Calculate Speed
            chs = []
            t1 = get_min_time(self.action_spd, team1.team)
            t2 = get_min_time(self.action_spd, team2.team)
            if t1 < t2:
                tmin = t1
            else:
                tmin = t2
            if tmin < 0 :
                tmin = 0
            for ich in team1.team:
                ich.spd_bar += ich.spd * tmin
                if ich.spd_bar >= self.action_spd:
                    chs.append(ich)
            for ich in team2.team:
                ich.spd_bar += ich.spd * tmin
                if ich.spd_bar >= self.action_spd:
                    chs.append(ich)
            # Someone should move this turn.
            if len(chs) > 0 :
                rch = random_pick(chs)
                rch.spd_bar -= self.action_spd
                if rch.team_flag == 1:
                    friends = team1
                    enemies = team2
                else:
                    friends = team2
                    enemies = team1
                recorder.set_team_flag(rch.team_flag)
                # AI Calculation
                for ai in rch.ai_list:
                    if ai.statified(rch, friends.team, enemies.team):
                        # skill applied
                        skill_applied(ai.tigger_skill, rch, friends, enemies, recorder)
                        break
                # Clean Battle
                team1.move_all_dead(recorder)
                team2.move_all_dead(recorder)
            turn += 1 # increase Turn No.
        return recorder
