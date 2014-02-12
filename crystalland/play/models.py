from django.db import models

# Create your models here.
class AccountDB(models.Model):
    user_name = models.CharField(max_length=64, unique=True)
    password  = models.CharField(max_length=64)

    def __unicode__ (self):
        return user_name
