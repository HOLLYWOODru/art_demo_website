from django.conf.urls import patterns, url
from .views import EventDetailView, PastEventListView, FutureEventListView

events_urlpatterns = patterns('',
    url(r'^events/(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='events.detail'),
    url(r'^events/past$', PastEventListView.as_view(), name='events.past'),
    url(r'^events/past?([\w-]+)$', PastEventListView.as_view(), name='events.past'),
    url(r'^events/future', FutureEventListView.as_view(), name='events'),
    url(r'^events/future?([\w-]+)/$', FutureEventListView.as_view(), name='events'),
)
