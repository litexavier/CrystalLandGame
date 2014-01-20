from models import MonsterDB
import skills

class Character(object):
    def __init__(self):
        self.name = ""
        self.maxhp = 0 # Max Heal Points
        self.hp = 0 # Heal Points
        self.maxsp = 0 # Max Spirit Points
        self.sp = 0 # Spirit Points
        self.atk = 0 # Attack
        self.matk = 0 # Magic Attack
        self._def = 0 # Defence
        self.mdef = 0 # Magic Defence
        self.acc = 0 # Accuracy
        self.blk = 0 # Block
        self.spd = 0 # Speed
        self.cri = 0 # Critical Hit Rate, 0-100, %
        self.per = 0 # Pierce, 0-100, %
        self.mper = 0 # Magic Pierce, 0-100, %
        self.ptt_rate = 0 # Protect Rate

class Monster(Character):
    def __init__ (self, id):
        self.mid = id
        # Generate from MonsterDB
        mon = MonsterDB.objects.get(mid=id)
        self.name = mon.name
        self.maxhp = mon.maxhp
        self.hp = mon.maxhp
        self.maxsp = mon.maxsp
        self.sp = mon.maxsp
        self.atk = mon.atk
        self.matk = mon.matk
        self._def = mon._def
        self.mdef = mon.mdef
        self.acc = mon.acc
        self.blk = mon.blk
        self.spd = mon.spd
        self.cri = mon.cri
        self.per = mon.per
        self.mper = mon.mper
        self.pos = 1 # 0 for front, 1 for back

    def setfront(self, rate_prot=0):
        self.pos = 0
        self.prot_rate = rate_prot
        # AIs
#        self.ai_list = []
#        for b in mon.ai.split(','):
#            arr = b.split('|')
#            sk = skills.skilllist[int(arr[2])](logrec)
#            self.ai_list.append(actionmode.actionmodelist[int(arr[0])](arr[1], sk)) 
