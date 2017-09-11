from django.conf.urls import patterns, url
from .views import ArtistsView, ArtistView, PhotographersView, TattooistsView, ArtistWorksView

core_urlpatterns = patterns('',
    url(r'^persons/artists/$', ArtistsView.as_view(), name='core.artists'),
    url(r'^persons/artists?([\w-]+)/$$', ArtistsView.as_view(), name='core.artists'),
    url(r'^persons/photographers/$', PhotographersView.as_view(), name='core.photographers'),
    url(r'^persons/photographers?([\w-]+)/$$', PhotographersView.as_view(), name='core.photographers'),
    url(r'^persons/tattooists/$', TattooistsView.as_view(), name='core.tattooists'),
    url(r'^persons/tattooists?([\w-]+)/$$', TattooistsView.as_view(), name='core.tattooists'),

    url(r'^(?P<username>[\w-]+)/$', ArtistWorksView.as_view(), name='core.artist'),
    url(r'^(?P<username>[\w-]+)/works/$', ArtistWorksView.as_view(), name='core.artist_works'),
    url(r'^(?P<username>[\w-]+)/works?([\w-]+)/$', ArtistWorksView.as_view(), name='core.artist_works'),
    url(r'^(?P<username>[\w-]+)/about/$', ArtistView.as_view(), name='core.artist_about'),
)
