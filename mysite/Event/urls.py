from django.conf.urls import url
from . import views

app_name = 'Event'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/homepage/event-details
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'Event/add/$',views.EventCreate.as_view(), name='Event-add'),
]
