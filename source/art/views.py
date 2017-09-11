from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Work

class WorksView(ListView):

    model = Work
    context_object_name = "works"
    template_name = "art/works.html"
    paginate_by = settings.WORKS_COUNT_ON_PAGE

    def get_queryset(self):
        works = Work.objects.order_by('-creation_date')

        return works


class WorkView(DetailView):

    model = Work
    context_object_name = "work"
    template_name = "art/work_detail.html"
