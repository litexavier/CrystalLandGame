# -*- coding: cp936 -*-
# Skills

import random
from gameutils import random_pick
from abc import ABCMeta, abstractmethod

def random_roll(perc):
    if random.random() < perc:
        return True
    else:
        return False
    
def choose_target(team, protect_allow = True):
    target = random_pick(team)
    target.prot_per = ""
    if protect_allow and target.pos == 1:
        for char in team:
            if char != target and char.pos == 0 and random_roll(char.prot_rate):
                char.prot_per = target.name
                target = char
                break
    return target

def phy_damage_calc(ATK, DMR, PERC, DEF, CRI, ACC, BLK):
    # Critical Hit
    is_cri = 0
    if random_roll(CRI/100.0):
        DMR = DMR * 2
        is_cri = 1
    # Miss
    block_rate = 0
    if ACC + BLK > 0 :
        block_rate = BLK * 1.0 / ( ACC + BLK )
    if random_roll(block_rate):
        return [is_cri, 0]
    RDM = ATK * DMR * (100 - PERC) / 100
    PDM = ATK * DMR * PERC / 100
    if RDM + DEF <= 0 :
        return [is_cri, RDM]
    else:
        return [is_cri, RDM * RDM / (RDM + DEF) + PDM]

class Skill(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__ (self, logrec): pass

    @abstractmethod
    def applied(self, tiggered_char, friends, enemies): pass

class NormalAttackSkill(object):
    name = "普通攻击".decode("cp936")
    id   = 0
    
    def applied(self, tiggered_char, friends, enemies, logrec):
        logrec.useskill(tiggered_char.name, self.name)
        target = choose_target(enemies)
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
    name = "爪击".decode("cp936")
    id   = 1

    def applied(self, tiggered_char, friends, enemies, logrec):
        if tiggered_char.sp < 2:
            print tiggered_char.sp
            logrec.failuseskill(tiggered_char.name)
            return False
        tiggered_char.sp -= 2
        logrec.useskill(tiggered_char.name, self.name)
        for loop in range(0,2):
            target = choose_target(enemies)
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
