from django.conf.urls import url
from . import views

app_name = 'Event'


urlpatterns = [
    url(r'^$', views.index, name='index'),

    #/homepage/event-details
    url(r'^(?P<Event_detail>[0-9]+)/$', views.detail, name='detail'),
]
