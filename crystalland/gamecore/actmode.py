# -*- coding: cp936 -*-
# Actions for AI

from abc import ABCMeta, abstractmethod

class ActionMode(object):
    __metaclass__ = ABCMeta

    def __init__ (self, param, tigger_skill):
        self.param = param
        self.tigger_skill = tigger_skill

    @abstractmethod
    def statified(self, tiggered_char, friends, enemies): pass
    
class ActionModeAL(ActionMode):
    name="总是".decode('cp936')
    id=0
    def statified(self, tiggered_char, friends, enemies):
        return True

# self hp less than param, run tigger_skill
class ActionModeSHPL(ActionMode):
    name="当自己的HP小于XX时".decode('cp936')
    id=1
    def statified(self, tiggered_char, friends, enemies):
        if tiggered_char.hp < int(self.param):
            return True
        else:
            return False

# self hp greater than param, run tigger_skill
class ActionModeSHPG(ActionMode):
    name="当自己的HP大于XX时".decode('cp936')
    id=2
    def statified(self, tiggered_char, friends, enemies):
        if tiggered_char.hp > int(self.param):
            return True
        else:
            return False


# self sp greater than param, run tigger_skill
class ActionModeSSPG(ActionMode):
    name="当自己的SP大于XX时".decode('cp936')
    id=3
    def statified(self, tiggered_char, friends, enemies):
        if tiggered_char.sp > int(self.param):
            return True
        else:
            return False

# self sp less than param, run tigger_skill
class ActionModeSSPL(ActionMode):
    name="当自己的SP小于XX时".decode('cp936')
    id=4
    def statified(self, tiggered_char, friends, enemies):
        if tiggered_char.sp < int(self.param):
            return True
        else:
            return False

# register action mode
actionmodelist = [ ActionModeAL, ActionModeSHPL, ActionModeSHPG, ActionModeSSPG, ActionModeSSPL ]
