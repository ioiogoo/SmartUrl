from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    Lurl = models.CharField(max_length=256)
    Surl = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return '<Url %s>' % self.Lurl

