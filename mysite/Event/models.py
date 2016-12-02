from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class Event(models.Model):
    """incharge of creating of the events"""
    Event_title = models.CharField(max_length=200)
    Location = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    Event_type = models.CharField(max_length=300)
    Event_topic = models.CharField(max_length=250)
    Event_image = models.FileField(null=False, blank=False)
    Event_detail = models.CharField(max_length=1000)
    Organizer_name = models.CharField(max_length=100,null=False)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


    def get_absolute_url(self):
        """returns the detail page"""
        return reverse('Event:detail', kwargs={'pk':self})


    def __unicode__(self):
        return self.Event_title

    def __str__(self):
        return self.Event_title





