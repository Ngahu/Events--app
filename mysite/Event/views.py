from django.views import generic
from .models import CreateEvent


class IndexView(generic.ListView):
    """incharge of returning the home page """
    template_name = 'Event/index.html'

    def get_queryset(self):
        """query the db to get a list of all the events"""
        return CreateEvent.objects.all()


class DetailView(generic.DetailView):
    """incharge of the events details"""
    model = CreateEvent
    template_name = 'Event/detail.html'