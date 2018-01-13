from django.conf.urls import url

import views

urlpatterns = [
    url(r'create/job/$', views.postjob, name='createjob'),
    url(r'joblist/$', views.joblist, name='joblist'),
    url(r'joblist/post/(?P<post_id>\d+)/$', views.jobpost, name='jobpost'),
]