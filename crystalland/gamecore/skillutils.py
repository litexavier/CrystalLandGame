import gameutils

# Target Selectors
class enemies_select_with_protect(object):
    def do(skill, tiggered_char, friends, enemies):
        target = gameutils.random_pick(enemies)
        target.prot_per = ""
        if target.pos == 1:
            for char in enemies:
                if char != target and char.pos == 0 and gameutils.random_roll(char.prot_rate):
                    char.prot_per = target.name
                    target = char
                    break
        return target

class select_friends_team(object):
    def do(skill, tiggered_char, friends, enemies):
        return friends

# Cost Applier
class none_cost_applied(object):
    def do(self, tiggered_char):
        return True

class sp_cost_applied(object):
    def __init__(self, cost):
        self.cost = cost
    def do(self, tiggered_char):
        if tiggered_char.sp < self.cost:
            return False
        tiggered_char.sp -= self.cost
        return True 
