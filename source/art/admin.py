from django.contrib import admin
from .models import Work, Tag


# registering Admin Model for Work
class WorkAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Primary',         {'fields': ['name', 'image_url', 'thumbnail_url', 'artist', 'creation_date', 'status']}),
        ('Secondary',       {'fields': ['information', 'colors', 'tags', 'artist_likes'], 'classes': ['collapse']}),
        ('Categories',      {'fields': ['form_of_art', 'genre_of_art', 'technique_of_art', 'style_of_art']}),
    ]

    list_display = ('name', 'artist', 'creation_date')
    list_filter = ('name', 'artist', 'creation_date')
    search_fields = ('name', 'artist')

admin.site.register(Work, WorkAdmin)

# registering Admin Model for Tag
class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)