from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Artist
from art.models import Work
from django.http import Http404


class ArtistsView(ListView):

    model = Artist
    context_object_name = "artists_list"
    template_name = "core/artists.html"
    paginate_by = settings.ARTISTS_COUNT_ON_PAGE

    def get_queryset(self):

        artists_list = Artist.objects.order_by('-date_joined')

        return artists_list


class PhotographersView(ListView):

    model = Artist
    context_object_name = "artists_list"
    template_name = "core/artists.html"
    paginate_by = settings.ARTISTS_COUNT_ON_PAGE

    def get_queryset(self):

        return []


class TattooistsView(ListView):

    model = Artist
    context_object_name = "artists_list"
    template_name = "core/artists.html"
    paginate_by = settings.ARTISTS_COUNT_ON_PAGE

    def get_queryset(self):

        return []


class ArtistView(DetailView):

    model = Artist
    template_name = "core/artist_about.html"

    def get_object(self):

        artist_username = self.kwargs['username']

        try:
            artist = Artist.objects.get(username=artist_username)
        except Artist.DoesNotExist:
            raise Http404("Художник с ником %s не найден", artist_username)

        return artist


class ArtistWorksView(ListView):

    model = Work
    context_object_name = "artist_works"
    template_name = "core/artist_works.html"
    paginate_by = settings.WORKS_COUNT_ON_PAGE

    def get_queryset(self):

        artist_username = self.kwargs['username']

        try:
            artist = Artist.objects.get(username=artist_username)
        except Artist.DoesNotExist:
            raise Http404("Художник с ником %s не найден", artist_username)

        artist_works = artist.works.all().order_by('-creation_date')

        return artist_works

    def get_context_data(self, **kwargs):

        artist_username = self.kwargs['username']

        try:
            artist = Artist.objects.get(username=artist_username)
        except Artist.DoesNotExist:
            raise Http404("Художник с ником %s не найден", artist_username)

        context = super(ArtistWorksView, self).get_context_data(**kwargs)
        context['artist'] = artist

        return context
