from django.db import models
import play_settings

class EquipStatement (object):
    def __init__ (self, attr_name, attr_delta):
        self.attr_name = attr_name
        self.attr_delta = attr_delta

    def do (self, target):
        p = getattr(target, self.attr_name)
        p = p + self.attr_delta
        setattr(target, self.attr_name, p)

    def undo (self, target):
        p = getattr(target, self.attr_name)
        p = p - self.attr_delta
        setattr(target, self.attr_name, p)

    def toString (self):
        return "%s,%s" % ( self.attr_name, self.attr_delta )

class MercenaryDB(models.Model):
    # Basic Info
    name = models.CharField(max_length=64)
    cl   = models.CharField(max_length=16) # Class
    lv   = models.IntegerField(default=0)       # Level
    exp  = models.IntegerField(default=0)       # Experience
    dpf  = models.SmallIntegerField(default=0)  # Is dispatched or not
    apts = models.SmallIntegerField(default=0) # Avaliable Dispatching Points
    # Attributes
    maxhp = models.IntegerField()
    maxsp = models.IntegerField()
    atk = models.IntegerField()
    matk = models.IntegerField()
    _def = models.IntegerField()
    mdef = models.IntegerField()
    acc = models.IntegerField(default=100)
    blk = models.IntegerField(default=0)
    spd = models.IntegerField()
    cri = models.IntegerField(default=0)
    per = models.IntegerField(default=0)
    mper = models.IntegerField(default=0)
    _str = models.IntegerField() # Main Attribute
    _vit = models.IntegerField() # Main Attribute
    _int = models.IntegerField() # Main Attribute
    ailvl = models.IntegerField(default=1)
    handle = models.IntegerField(default=10)
    # Equipments
    eq_LH = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Left Hand
    eq_RH = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Right Hand
    eq_HD = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Head
    eq_BD = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Body
    eq_BT = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Boot
    eq_R1 = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Ring 1
    eq_R2 = models.ForeignKey('Equipment', related_name='+', null='True', on_delete=models.SET_NULL) # Ring 2
    def expUp(self, exp_plus):
        self.exp += exp_plus
        old_lv = self.lv
        while self.lv < play_settings.MAXMERCENARY_LEVEL_ALLOWED and self.exp >= play_settings.EXPERIENCE_LEVEL_UP_TABLE[self.lv+1]:
            self.exp -= play_settings.EXPERIENCE_LEVEL_UP_TABLE[self.lv+1]
            self.lvlUp(self)
    def lvlUp(self):
        tab = play_settings.CLASS_FEATURE_TABLE[self.cl]
        self.lv += 1
        self.apts += play_settings.DISPATCHING_POINTS_PER_LEVEL
    def strUp(self):
        tab = play_settings.CLASS_FEATURE_TABLE[self.cl]
        if self.apts <= 0:
            return False
        self.apts -= 1
        self._str += 1
        self.atk += tab['atkinc']
        self._def += tab['definc']
        return True
    def vitUp(self):
        tab = play_settings.CLASS_FEATURE_TABLE[self.cl]
        if self.apts <= 0:
            return False
        self.apts -= 1
        self._vit += 1
        self.maxhp += tab['hpinc']
        self.maxsp += tab['spinc']
        return True
    def intUp(self):
        tab = play_settings.CLASS_FEATURE_TABLE[self.cl]
        if self.apts <= 0:
            return False
        self.apts -= 1
        self._int += 1
        self.matk += tab['matkinc']
        self.mdef += tab['mdefinc']
        return True
    def getEquip(self, eq, pos):
        if pos == 'LH':
            eq_LH = eq
        elif pos == 'RH':
            eq_RH = eq
        elif pos == 'HD':
            eq_HD = eq
        elif pos == 'BD':
            eq_BD = eq
        elif pos == 'BT':
            eq_BT = eq
        elif pos == 'R1':
            eq_R1 = eq
        elif pos == 'R2':
            eq_R2 = eq
        else:
            return False
        eq.decode_stat()
        for i in eq.statement_de:
            i.do(self)
        return True
    def dropEquip(self, pos):
        eq = None;
        if pos == 'LH':
            eq = eq_LH
        elif pos == 'RH':
            eq = eq_RH
        elif pos == 'HD':
            eq = eq_HD
        elif pos == 'BD':
            eq = eq_BD
        elif pos == 'BT':
            eq = eq_BT
        elif pos == 'R1':
            eq = eq_R1
        elif pos == 'R2':
            eq = eq_R2
        else:
            return False
        eq.decode_stat()
        for i in eq.statement_de:
            i.undo(this)
        return True
    def __unicode__(self):
        return self.name

class GuildDB(models.Model):
    id    = models.IntegerField(primary_key = True)
    name  = models.CharField(max_length=64, unique=True)
    gold  = models.IntegerField()
    honor = models.IntegerField()
    mercenaries = models.ManyToManyField(MercenaryDB)
    items = models.TextField(default="")
    def __unicode__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=64, unique=True)
    price = models.IntegerField()
    equip_type = models.CharField(max_length=8)
    equip_class = models.CharField(max_length=8)
    statement = models.TextField()
    handle = models.IntegerField()
    describe = models.CharField(max_length=128)
    dual_hand_flag = models.SmallIntegerField()
    dur    = models.IntegerField(default=-1)
    shopsell = models.SmallIntegerField(default=0)

    def dur_loss(self):
        if dur != -1:
            dur -= 1
            
    def decode_stat(self):
        self.statement_de = []
        for col in self.statement.split('|'):
            arr = col.split(',')
            self.statement_de.append(EquipStatement(arr[0], arr[1]))

    def encode_stat(self):
        self.statement = ""
        for col in self.statement_de:
            if self.statement != "" :
                self.statement += "|"
            self.statement += col.toString()

    def __unicode__ (self):
        return self.name
