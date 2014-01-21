import random

def random_pick(items):
    sz = len(items)
    if sz == 0:
        return None
    return items[random.randint(0, sz-1)]

def random_roll(perc):
    if random.random() < perc:
        return True
    else:
        return False
    
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

def magic_damage_calc(MATK, DMR, PERC, MDEF, CRI, ACC, BLK):
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
    RDM = MATK * DMR * (100 - PERC) / 100
    PDM = MATK * DMR * PERC / 100
    if RDM + MDEF <= 0 :
        return [is_cri, RDM]
    else:
        return [is_cri, RDM * RDM / (RDM + MDEF) + PDM]
