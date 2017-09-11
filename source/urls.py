from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.urls import core_urlpatterns
from registration.urls import register_urlpatterns
from art.urls import art_urlpatterns
from articles.urls import articles_urlpatterns
from events.urls import events_urlpatterns
from user.urls import user_urlpatterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += user_urlpatterns
urlpatterns += articles_urlpatterns
urlpatterns += events_urlpatterns
urlpatterns += art_urlpatterns
urlpatterns += register_urlpatterns
urlpatterns += core_urlpatterns
