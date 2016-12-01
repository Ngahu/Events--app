from django.conf.urls import url
from . import views

app_name = 'Event'


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
