# -*- coding: utf-8 -*-
# Skills

import random
import gameutils, skillutils, actmode
from debuffstats import Poison
from char import Monster

class NormalAttackSkill(object):
    name = "普通攻击".decode("utf-8")
    describe = "对目标敌人造成100%的物理伤害".decode("utf-8")
    id   = 0
    selector = skillutils.enemies_select_with_protect()
    times = 1
    prepare_time = 0
    delay_time = 0
    damage_type = 2
    cost = skillutils.none_cost_applied()
 
    def applied(self, tiggered_char, target, logrec):
        # Actual Attack Damage Calculate
        dmg_c = gameutils.phy_damage_calc(tiggered_char.atk, 1, tiggered_char.per, target._def, tiggered_char.cri, tiggered_char.acc, target.blk)
        dmg = dmg_c[1]
        # Applied Damage
        if target.hp < dmg:
            dmg = target.hp
        target.hp -= dmg
        logrec.damaged(target.name, dmg, target.prot_per, dmg_c[0])
        return True

class ClawAttackSkill(object):
    name = "爪击".decode("utf-8")
    describe = "对目标造成100%的物理伤害".decode("utf-8")
    id   = 1
    selector = skillutils.enemies_select_with_protect()
    times = 2
    prepare_time = 10
    delay_time = 0
    damage_type = 2
    cost = skillutils.sp_cost_applied(2)        
    
    def applied(self, tiggered_char, target, logrec):
        # Actual Attack Damage Calculate
        dmg_c = gameutils.phy_damage_calc(tiggered_char.atk, 1, tiggered_char.per, target._def, tiggered_char.cri, tiggered_char.acc, target.blk)
        dmg = dmg_c[1]
        # Applied Damage
        if target.hp < dmg:
            dmg = target.hp
        target.hp -= dmg
        logrec.damaged(target.name, dmg, target.prot_per, dmg_c[0])
        return True

class PoisonSkill(object):
    name = "下毒".decode("utf-8")
    describe = "使目标中毒，每回合造成5点魔法伤害，持续5回合".decode("utf-8")
    id = 2
    selector = skillutils.enemies_select_with_protect()
    times = 1
    prepare_time = 0
    delay_time = 120
    damage_type = 1
    cost = skillutils.sp_cost_applied(10)

    def applied(self, tiggered_char, target, logrec):
        target.attach_status.append(Poison(5))
        logrec.stat_attach(target.name, Poison.name)
        return True

class SummonSpirit(object):
    name = "召唤精灵".decode("utf-8")
    describe = "召唤一只精灵加入战斗".decode("utf-8")
    id = 3
    selector = skillutils.select_friends_team()
    times = 1
    prepare_time = 20
    delay_time = 0
    damage_type = 2
    cost = skillutils.sp_cost_applied(10)

    def applied(self, tiggered_char, target, logrec):
        mon = Monster(1001)
        if tiggered_char.pos == 0:
            mon.setfront()
        # Set AI
        mon.ai_list = [actmode.ActionModeAL("", NormalAttackSkill())]
        # To battle
        mon.team_flag = tiggered_char.team_flag
        mon.attach_status = []
        mon.team_obj  = tiggered_char.team_obj
        mon.alive = True
        mon.spd_bar = 0
        mon.stage = 0
        target.append(mon)
        
# register skills
skilllist = [ NormalAttackSkill, ClawAttackSkill, PoisonSkill, SummonSpirit]
