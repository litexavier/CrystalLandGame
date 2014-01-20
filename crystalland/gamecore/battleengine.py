from logrec import BattleRecorder
from gameutils import random_pick

def reset_speed_bar(team):
    for ch in team:
        ch.spd_bar = 0

def set_team_flag(team, flag):
    for ch in team:
        ch.team_flag = flag

def set_all_alive(team):
    for ch in team:
        if ch.hp > 0:
            ch.alive = True
        else:
            ch.alive = False

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

class BattleEngine(object):
    def __init__ (self, maxturn, action_spd):
        self.maxturn = maxturn
        self.action_spd = action_spd
        self.broadcastturn = 10
        
    def battle(self, team1, team2):
        recorder = BattleRecorder () # create a new battle recorder
        # start battle
        turn = 1
        reset_speed_bar(team1)
        reset_speed_bar(team2)
        set_team_flag(team1, 1)
        set_team_flag(team2, 2)
        set_all_alive(team1)
        set_all_alive(team2)
        dead_team1 = []
        dead_team2 = []
        team1 = move_dead_char(team1, dead_team1, recorder)
        team2 = move_dead_char(team2, dead_team2, recorder)
        while turn <= self.maxturn:
            al1 = len(team1)
            al2 = len(team2)
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
                recorder.broadcast(turn, team1, dead_team1, team2, dead_team2)
            # Calculate Speed
            chs = []
            t1 = get_min_time(self.action_spd, team1)
            t2 = get_min_time(self.action_spd, team2)
            if t1 < t2:
                tmin = t1
            else:
                tmin = t2
            if tmin < 0 :
                tmin = 0
            for ich in team1:
                ich.spd_bar += ich.spd * tmin
                if ich.spd_bar >= self.action_spd:
                    chs.append(ich)
            for ich in team2:
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
                    if ai.statified(rch, friends, enemies):
                        # skill applied
                        ai.tigger_skill.applied(rch, friends, enemies, recorder)
                        break
                # Clean Battle
                team1 = move_dead_char(team1, dead_team1, recorder)
                team2 = move_dead_char(team2, dead_team2, recorder)
            turn += 1 # increase Turn No.
        return recorder
