from django.db import models

class EquipStatement (object):
    def __init__ (self, attr_name, attr_delta):
        self.attr_name = attr_name
        self.attr_delta = attr_delta

    def do (self, target):
        p = getattr(target, self.attr_name)
        p = p + self.attr_delta
        setattr(target, self.attr_name, p)

    def toString (self):
        return "%s,%s" % ( self.attr_name, self.attr_delta )

class GuildDB(models.Model):
    id    = models.IntegerField(primary_key = True)
    name  = models.CharField(max_length=64, unique=True)
    gold  = models.IntegerField()
    honor = models.IntegerField()

    def __unicode__(self):
        return self.name
    
class MercenaryDB(models.Model):
    # Basic Info
    name = models.CharField(max_length=64, unique=True)
    cl   = models.CharField(max_length=8) # Class
    lv   = models.IntegerField()       # Level
    exp  = models.IntegerField()       # Experience
    dpf  = models.SmallIntegerField()  # Is dispatched or not
    # Attributes
    maxhp = models.IntegerField()
    maxsp = models.IntegerField()
    atk = models.IntegerField()
    matk = models.IntegerField()
    _def = models.IntegerField()
    mdef = models.IntegerField()
    acc = models.IntegerField()
    blk = models.IntegerField()
    spd = models.IntegerField()
    cri = models.IntegerField()
    per = models.IntegerField()
    mper = models.IntegerField()
    _str = models.IntegerField() # Main Attribute
    _dex = models.IntegerField() # Main Attribute
    _vit = models.IntegerField() # Main Attribute
    _int = models.IntegerField() # Main Attribute
    # Equipments
    eq_LH = models.ForeignKey('Equipment', related_name='+') # Left Hand
    eq_RH = models.ForeignKey('Equipment', related_name='+') # Right Hand
    eq_HD = models.ForeignKey('Equipment', related_name='+') # Head
    eq_BD = models.ForeignKey('Equipment', related_name='+') # Body
    eq_BT = models.ForeignKey('Equipment', related_name='+') # Boot
    eq_R1 = models.ForeignKey('Equipment', related_name='+') # Ring 1
    eq_R2 = models.ForeignKey('Equipment', related_name='+') # Ring 2
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
    dur    = models.IntegerField()

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
