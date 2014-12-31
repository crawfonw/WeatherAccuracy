from django import template
from tracker.models import Query

register = template.Library()

@register.filter
def get_type(value):
    return type(value)

@register.assignment_tag
def latest_query(city_pk):
    q = Query.objects.filter(city_id=city_pk).order_by('-time_executed')
    if q.count():
        return q[0]
    return None

@register.simple_tag
def active(request, pattern):
    path = request.path
    if pattern == '/':
        if pattern == path:
            return 'active'
    elif pattern in path:
        return 'active'
    return ''