#uncteams app urls.py
from django.conf.urls.defaults import patterns, url

from uncteams import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='uncteams_home'),
    url(r'^athlete/$', views.athleteList, name='uncteams_athlete_list'),
    url(r'^team/(?P<pk>\d+)$', views.team, name='uncteams_team'),
    url(r'^athlete/(?P<pk>\d+)$', views.athlete, name='uncteams_athlete'),
    )

