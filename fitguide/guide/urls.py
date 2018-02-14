from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
        url(r'^$',views.blank, name = 'blank'),
        url(r'^login/$',login,{'template_name':'guide/login.html'}),
        url(r'^logout/$',logout,{'template_name':'guide/logout.html'}),
        url(r'^register/$',views.register,name  = 'register'),
        url(r'^profile/$',views.profile,name = 'profile'),
        url(r'^edit/$',views.editprofile,name = 'editprofile'),
        url(r'^schedule/$',views.schedule,name = 'schedule'),
]
