from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('processor/dashboard-base.html',
                              {'page_title': 'WeatherTracker | Dashboard',
                               'page_header': 'Home',
                               'page_lead': 'Stuff will be here!',
                               },
                               RequestContext(request))
