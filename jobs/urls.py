from django.conf.urls import url

import views

urlpatterns = [
    url(r'create/job/', views.postjob, name='createjob')
]