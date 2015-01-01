from django.conf.urls import patterns, include, url

from querier import query_func_map
q_type_allowed_chars = ''.join(query_func_map.keys() + \
                               map(str.lower, query_func_map.keys())) 

urlpatterns = patterns('tracker.views',
    #url(r'^$', 'index', name='tracker-index'),
    url(r'^history/$', 'query_history', name='query-history'),
    url(r'^latest/$', 'latest_query', name='latest-query-history'),
    url(r'^query/(?P<query_id>[\d]+).json', 'display_query', name='query-lookup'),
    url(r'^query/new/(?P<q_type>[%s])/(?P<city_id>[\d]+)/$' % q_type_allowed_chars, \
            'query_city_weather', name='new-weather-query'),
)