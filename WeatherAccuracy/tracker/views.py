from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone

from models import City, Query

from querier import query_func_map

def index(request):
    return render_to_response('tracker/index.html',
                              {'page_title': 'WeatherTracker',
                               'page_header': 'Home',
                               'page_lead': 'Stuff will be here!',
                               },
                               RequestContext(request))

def latest_query(request):
    cities = City.objects.all().order_by('pk')
    return render_to_response('tracker/latest-query-history.html',
                              {'page_title': 'WeatherTracker | History',
                               'page_header': "Cities' Most Recent Queries",
                               'cities': cities,
                               },
                               RequestContext(request))

def query_history(request):
    queries = Query.objects.order_by('-pk', '-time_executed')[:50]
    return render_to_response('tracker/query-history.html',
                              {'page_title': 'WeatherTracker | History',
                               'page_header': '50 Most Recent Queries',
                               'queries': queries,
                               },
                               RequestContext(request))

def display_query(request, query_id):
    q = get_object_or_404(Query, pk=query_id)
    return StreamingHttpResponse(str(q.raw_results), content_type='application/json')

def query_city_weather(request, q_type, city_id):
    q_type = q_type.upper()
    if q_type in query_func_map.keys():
        c = get_object_or_404(City, pk=city_id)
        q_string, data = query_func_map[q_type](c.city_id)
        q = Query.objects.create(city=c, time_executed=timezone.now(), full_query_string=q_string, \
                                 raw_results=data, query_type=q_type,)
        if data:
            q.was_success = True
            messages.success(request, 'Hooray! - %s (%s) successfully retrieved.' % (q, q.query_type))
        else:
            q.was_success = False
            messages.error(request, 'Oh noes! There was a problem querying %s (qs=%s).' % (c, q_string))
        q.save()
    return HttpResponseRedirect(reverse(latest_query))
        
    