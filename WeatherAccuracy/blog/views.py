from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import BlogPost

def _latest_blogpost():
    q = BlogPost.objects.filter(is_draft=False).order_by('-post_date')
    if q.count():
        return q[0]

def index(request):
    latest_post = _latest_blogpost()
    return render_to_response('blog/index.html',
                              {'page_title': 'WeatherTracker',
                               'page_header': 'Latest News',
                               'post': latest_post,
                               },
                               RequestContext(request))
    
def archive(request):
    blog_posts = BlogPost.objects.filter(is_draft=False)
    return render_to_response('blog/archive.html',
                              {'page_title': 'WeatherTracker | Archive',
                               'page_header': 'News Archive',
                               'posts': blog_posts,
                               },
                               RequestContext(request))
    
def archived_post(request, post_id):
    if BlogPost.objects.filter(pk=post_id).exists():
        post = BlogPost.objects.get(pk=post_id)
        if post.is_draft:
           return HttpResponseRedirect(reverse(index)) 
        return render_to_response('blog/archived-post.html',
                                  {'page_title': 'WeatherTracker | Archive',
                                   #'page_header': 'News Archive',
                                   'post': post,
                                   },
                                   RequestContext(request))
    return HttpResponseRedirect(reverse(index)) 