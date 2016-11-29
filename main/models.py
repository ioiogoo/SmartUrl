from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=256)

    def __str__(self):
        return '<Url %s>' % self.url
