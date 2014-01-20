# -*- coding: utf-8 -*-
# Skills

import random
import gameutils, skillutils

def phy_damage_calc(ATK, DMR, PERC, DEF, CRI, ACC, BLK):
    # Critical Hit
    is_cri = 0
    if gameutils.random_roll(CRI/100.0):
        DMR = DMR * 2
        is_cri = 1
    # Miss
    block_rate = 0
    if ACC + BLK > 0 :
        block_rate = BLK * 1.0 / ( ACC + BLK )
    if gameutils.random_roll(block_rate):
        return [is_cri, 0]
    RDM = ATK * DMR * (100 - PERC) / 100
    PDM = ATK * DMR * PERC / 100
    if RDM + DEF <= 0 :
        return [is_cri, RDM]
    else:
        return [is_cri, RDM * RDM / (RDM + DEF) + PDM]

class NormalAttackSkill(object):
    name = "普通攻击".decode("utf-8")
    describe="对目标敌人造成100%的物理伤害"
    id   = 0
    selector = skillutils.enemies_select_with_protect()
    times = 1
    prepare_time = 0
    delay_time = 0
    damage_type = 2
    cost = skillutils.none_cost_applied()
 
    def applied(self, tiggered_char, target, logrec):
        # Actual Attack Damage Calculate
        dmg_c = phy_damage_calc(tiggered_char.atk, 1, tiggered_char.per, target._def, tiggered_char.cri, tiggered_char.acc, target.blk)
        dmg = dmg_c[1]
        # Applied Damage
        if target.hp < dmg:
            dmg = target.hp
        target.hp -= dmg
        logrec.damaged(target.name, dmg, target.prot_per, dmg_c[0])
        return True

class ClawAttackSkill(object):
    name = "爪击".decode("utf-8")
    describe = "对目标造成100%的物理伤害"
    id   = 1
    selector = skillutils.enemies_select_with_protect()
    times = 2
    prepare_time = 10
    delay_time = 0
    damage_type = 2
    cost = skillutils.sp_cost_applied(2)        
    
    def applied(self, tiggered_char, target, logrec):
        # Actual Attack Damage Calculate
        dmg_c = phy_damage_calc(tiggered_char.atk, 1, tiggered_char.per, target._def, tiggered_char.cri, tiggered_char.acc, target.blk)
        dmg = dmg_c[1]
        # Applied Damage
        if target.hp < dmg:
            dmg = target.hp
        target.hp -= dmg
        logrec.damaged(target.name, dmg, target.prot_per, dmg_c[0])
        return True

# register skills
skilllist = [ NormalAttackSkill, ClawAttackSkill, ]
