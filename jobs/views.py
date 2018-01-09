# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import JobPostForm
# Create your views here.

def postjob(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
        return redirect('home')
    else:
        form = JobPostForm()
    return render(request, 'jobs/forms/jobpostform.html', {'form': form})

