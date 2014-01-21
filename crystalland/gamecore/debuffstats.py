# -*- coding: utf-8 -*-

import gameutils

class Poison(object):
    name = "中毒".decode('utf-8')
    def __init__(self, val):
        self.val = val

    def applied(self, target, logrec):
        dmg_c = gameutils.magic_damage_calc(self.val, 1, 0, target._def, 0, 100, 0)
        dmg = dmg_c[1]
        # Applied Damage
        if target.hp < dmg:
            dmg = target.hp
        target.hp -= dmg
        logrec.stat_run(self.name, target.name, dmg)

