# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    bio = models.TextField(max_length=500, blank=True)
    profession = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.get_full_name()