# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from .forms import JobPostForm
from .models import JobPost, JobStatus
# Create your views here.

def joblist(request):
    jobs = JobPost.objects.all()
    return render(request, 'jobs/joblist.html', {'jobs': jobs})

def postjob(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = User.objects.get(pk=request.user.id)
            job.status = JobStatus.objects.get(pk=1)
            job.save()
            return redirect('joblist')
    else:
        form = JobPostForm()
    return render(request, 'jobs/forms/jobpostform.html', {'form': form})

def jobpost(request, post_id):
    jobpost = get_object_or_404(JobPost, pk=post_id)
    return render(request, 'jobs/jobpost.html', {'jobpost': jobpost})
