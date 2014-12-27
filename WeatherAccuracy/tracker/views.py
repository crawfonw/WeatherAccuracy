from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import timezone

from models import City, Query

from querier import current_weather_for

def index(request):
    print reverse('tracker-index')
    return render_to_response('tracker/index.html',
                              {'page_title': 'WeatherTracker',
                               'page_header': 'Home',
                               'page_lead': 'Stuff will be here!',
                               },
                               RequestContext(request))

def latest_query(request):
    cities = City.objects.all()
    return render_to_response('tracker/latest-query-history.html',
                              {'page_title': 'WeatherTracker | History',
                               'page_header': "Cities' Most Recent Queries",
                               'cities': cities,
                               },
                               RequestContext(request))

def query_history(request):
    queries = Query.objects.order_by('-time_executed')[:50]
    return render_to_response('tracker/query-history.html',
                              {'page_title': 'WeatherTracker | History',
                               'page_header': '50 Most Recent Queries',
                               'queries': queries,
                               },
                               RequestContext(request))

def display_query(request, query_id):
    q = get_object_or_404(Query, pk=query_id)
    return StreamingHttpResponse(str(q.raw_results), content_type='application/json')

def query_city_current_weather(request, city_id):
    c = get_object_or_404(City, pk=city_id)
    q_string, data = current_weather_for(c.city_id)
    q = Query.objects.create(city=c, time_executed=timezone.now(), full_query_string=q_string, \
                             raw_results=data, query_type='C',)
    if data:
        q.was_success = True
        messages.success(request, 'Hooray! - %s (%s) successfully retrieved.' % (q, q.query_type))
    else:
        q.was_success = False
        messages.error(request, 'Oh noes! There was a problem querying %s (qs=%s).' % (c, q_string))
    q.save()
    return HttpResponseRedirect(reverse(latest_query))
    