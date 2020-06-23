from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
]