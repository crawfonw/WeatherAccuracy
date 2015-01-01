from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from tracker.models import City, Query
from tracker.querier import query_func_map

#1.7 and under
class Command(BaseCommand):
    args = '<[c] [d] [h]>'
    help = 'Queries the weather api for each city in the db'

#options for 1.8
#     def add_arguments(self, parser):
#         parser.add_argument('c', action='store_true', help='Get current weather', default=False)
#         parser.add_argument('h', action='store_true', help='Get hourly forecast weather', default=False)
#         parser.add_argument('f', action='store_true', help='Get daily forecast weather', default=False)

    def handle(self, *args, **options):
        args = map(str.upper, args)
        cities = City.objects.all()
        for opt in args:
            if opt in dict(Query.QUERY_TYPES).keys():
                for c in cities:
                    q_string, data = query_func_map[opt](c.city_id)
                    q = Query.objects.create(city=c, time_executed=timezone.now(), \
                                             full_query_string=q_string, query_type=opt, \
                                             picked_up_by_processor=False)
                    if data:
                        q.was_success = True
                        q.raw_results = data
                    else:
                        q.was_success = False
                        q.raw_results = ''
                    q.save()
        self.stdout.write('Ran queries command')