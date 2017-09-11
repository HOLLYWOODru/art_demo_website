from django.contrib import admin
from .models import Artist

class ArtistAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Primary',                 {'fields': ['username', 'first_name', 'last_name', 'email', 'password', 'is_activated']}),
        ('Secondary',               {'fields': ['avatar_url', 'site_url', 'twitter_name', 'information']}),
        ('Date information',        {'fields': ['birth_date', 'date_joined', 'last_login']}),
        ('Artifex information',     {'fields': ['has_artifex_article', 'artifex_article_url']}),
    ]

    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_filter = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')


admin.site.register(Artist, ArtistAdmin)