from django.conf.urls import patterns, url
from .views import WorkView, WorksView

art_urlpatterns = patterns('',
    url(r'^works/(?P<pk>[0-9]+)/$', WorkView.as_view(), name='art.work'),
    url(r'^works/$', WorksView.as_view(), name='art.works'),
    url(r'^works?([\w-]+)/$', WorksView.as_view(), name='art.works'),
)
