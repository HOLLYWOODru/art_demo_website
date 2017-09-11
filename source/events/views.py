from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Event
import datetime


class PastEventListView(ListView):

    model = Event
    context_object_name = "events"
    template_name = "events/events.html"
    paginate_by = settings.EVENTS_COUNT_ON_PAGE

    def get_queryset(self):
        events = Event.objects.filter(end_time__lte=datetime.date.today()).order_by('-start_time')

        return events


class FutureEventListView(ListView):

    model = Event
    context_object_name = "events"
    template_name = "events/events.html"
    paginate_by = settings.EVENTS_COUNT_ON_PAGE

    def get_queryset(self):
        events = Event.objects.filter(end_time__gte=datetime.date.today()).order_by('-start_time')

        return events


class EventDetailView(DetailView):

    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"
