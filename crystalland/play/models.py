from django.db import models

class GuildDB(models.Model):
    id    = models.IntegerField(primary_key = True)
    name  = models.CharField(max_length=64, unique=True)
    gold  = models.IntegerField()
    honor = models.IntegerField()

    def __unicode__(self):
        return self.name
