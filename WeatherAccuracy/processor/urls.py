from django.conf.urls import patterns, include, url 

urlpatterns = patterns('processor.views',
    url(r'^', 'index', name='processor-index'),
)