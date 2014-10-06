from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('conference.views',
    url(r'^$', index, name='tracker-index'),
    url(r'^query/(?P<query_id>[\d]+)/$', display_query, name='query-lookup'),
    url(r'^query/new/weather/(?P<city_id>[\d]+)/$', query_city_weather, name='new-weather-query')
)