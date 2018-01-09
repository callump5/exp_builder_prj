# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=70)
    user = models.OneToOneField(User, related_name='job_post')
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title