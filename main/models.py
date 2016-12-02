# *-* coding:utf-8 *-*
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Url(models.Model):
    Lurl = models.CharField(max_length=255, unique=True)
    Surl = models.CharField(max_length=32, blank=True)
    Views = models.IntegerField(max_length=32, default=0)
    Date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return '<Url %s>' % self.Lurl

