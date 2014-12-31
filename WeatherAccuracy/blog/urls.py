from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='blog-index'),
    url(r'^archive/$', 'archive', name='blog-history'),
    url(r'^archive/(?P<post_id>[\d]+)/$', 'archived_post', name='blog-history-post')
)