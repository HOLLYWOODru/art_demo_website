from django.conf.urls import patterns, url
from .views import ArtistProfileView, ArtistAboutView, ArtistPasswordView
from django.contrib.auth.decorators import login_required


user_urlpatterns = patterns('',
    url(r'^account/$', login_required(ArtistProfileView.as_view()), name='user.account.profile'),
    url(r'^account/about', login_required(ArtistAboutView.as_view()), name='user.account.about'),
    url(r'^account/password$', login_required(ArtistPasswordView.as_view()), name='user.account.password'),
)
