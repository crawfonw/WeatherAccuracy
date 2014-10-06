from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import City, Query

from datetime import datetime

import urllib2, urllib, json
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
#query = 'London,uk'

def _query(query):
    query_url = base_url + 'q=' + query
    result = urllib2.urlopen(query_url).read()
    data = json.loads(result)
    return query_url, data

def index(request):
    cities = City.objects.all()
    return render_to_response('tracker/index.html',
                              {'page_title': 'WeatherTracker',
                               'cities': cities,
                               },
                               RequestContext(request))

def display_query(request, query_id):
    q = get_object_or_404(Query, pk=query_id)
    return HttpResponse(q.raw_results, content_type='text/plain')

def query_city_weather(request, city_id):
    c = get_object_or_404(City, pk=city_id)
    q_string, data = _query(c.query_string)
    if data:
        Query.objects.create(city=c, time_executed=datetime.now(), full_query_string=q_string, raw_results=data)
        messages.success(request, 'Hooray!')
    else:
        messages.error(request, 'Oh noes!')
    return index(request)
    