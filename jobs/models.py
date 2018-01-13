# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profession


# Create your models here.

class JobStatus(models.Model):
    status = models.CharField(max_length=20)

    def __unicode__(self):
        return self.status


class JobPost(models.Model):
    title = models.CharField(max_length=70)
    user = models.ForeignKey(User, related_name='job_post')
    category = models.ForeignKey(Profession, related_name='job_post')
    description = models.TextField(max_length=1000)
    status = models.ForeignKey(JobStatus.objects.get(pk=1), related_name='job_post')

    def __unicode__(self):
        return self.title.title()


class JobRequest(models.Model):
    job_id = models.ForeignKey(JobPost, related_name='job_request')
    applicant_id = models.ForeignKey(User, related_name='job_request')

    def __unicode__(self):
        return 'Title: ' + self.job_id.title + ' ID: ' + str(self.id)