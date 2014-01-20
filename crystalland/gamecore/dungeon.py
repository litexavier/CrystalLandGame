from models import DungeonDB
import json
import actmode,skills
from char import Monster

class Dungeon(object):
    def __init__(self):
        self.id = 0
        self.name = ""
        self.data = []
        self.resetbybattle = 1
        self.dg = None

    def load(self, did):
        self.dg = DungeonDB.objects.get(id=did)
        self.id = self.dg.id
        self.name = self.dg.name
        self.data = json.loads(self.dg.data)
        self.resetbybattle = self.dg.resetbybattle
        return self
        
    def save(self):
        if self.dg == None:
            self.dg = DungeonDB(name=self.name, data=json.dumps(self.data), resetbybattle = self.resetbybattle)
        else:
            self.dg.name = self.name
            self.dg.data = json.dumps(self.data)
            self.dg.resetbybattle = self.resetbybattle
        ret = True
        try:
            self.dg.save()
        except:
            ret = False
        return ret

    def addmon(self, monstr):
        mon = json.loads(monstr)
        self.data.append(mon)

    def delmon(self, monl):
        newdata = []
        for i in range(0, len(self.data)):
            if i != monl:
                newdata.append(self.data[i])
        self.data = newdata
        #del self.data[monl]

    def modmon(self, monl, mondata):
        mon = json.loads(mondata)
        self.data[monl] = mon

    def generateTeam(self):
        team = []
        for mon in self.data:
            m = Monster(mon["mid"])
            m.name = mon["mname"]
            if mon["pos"] == "0" :
                m.setfront(mon["protrate"])
            m.ai_list = []
            for aistr in mon["ai"]:
                m.ai_list.append(
                    actmode.actionmodelist[int(aistr["mode"])](aistr["val"],
                                                skills.skilllist[int(aistr["skill"])]()));
            team.append(m)
        return team
