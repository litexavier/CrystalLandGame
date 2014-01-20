from django.db import models
import json

# Create your models here.
class MonsterDB(models.Model):
    mid  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
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

    def __unicode__(self):
        return self.name

class DungeonDB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    data = models.TextField()
    resetbybattle = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.name
