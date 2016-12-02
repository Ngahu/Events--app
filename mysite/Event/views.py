from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Event


class IndexView(generic.ListView):
    """incharge of returning the home page """
    template_name = 'Event/index.html'

    def get_queryset(self):
        """query the db to get a list of all the events"""
        return Event.objects.all()


class DetailView(generic.DetailView):
    """incharge of the events details"""
    model = Event
    template_name = 'Event/detail.html'


class EventCreate(CreateView):
    """creating a new event"""
    model = Event
    fields = ['Event_title', 'Location', 'time', 'Event_type', 'Event_topic', 'Event_image', 'Event_detail', 'Organizer_name']



class EventUpdate(UpdateView):
    """incharge of updating the Created event"""
    model = Event
    fields = ['Event_title', 'Location', 'time', 'Event_type', 'Event_topic', 'Event_image', 'Event_detail','Organizer_name']



class EventDelete(DeleteView):
    """incharge of deleting event"""
    model = Event
    success_url = reverse_lazy('Event:index')