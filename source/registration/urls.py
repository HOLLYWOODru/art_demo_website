from django.conf.urls import patterns, url
from . import views

register_urlpatterns = patterns('',
    url(r'^signup/$', views.register_user, name='registration.signup'),
    url(r'^signin/$', views.log_in_user, name='registration.signin'),
    url(r'^logout/$', views.log_out_user, name='registration.logout'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirm),
)
