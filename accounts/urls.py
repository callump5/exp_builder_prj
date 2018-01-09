from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'signup/create-profile/$', views.makeprofile, name='createprofile'),
    url(r'logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'login/$', auth_views.login, name='login'),
]