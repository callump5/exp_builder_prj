# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from models import JobPost, JobStatus, JobRequest

# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobStatus)
admin.site.register(JobRequest)