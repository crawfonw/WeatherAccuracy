from django.contrib import admin

from WeatherAccuracy.shared_admin import FengShuiAdmin
from models import City, Query
    
class CityAdmin(FengShuiAdmin):
    list_display = ('name', 'city_id',)
    
class QueryAdmin(FengShuiAdmin):
    list_display = ('city', 'time_executed', 'full_query_string', 'was_success',)
    list_filter = ('was_success',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [x.name for x in obj._meta.fields]
        return self.readonly_fields

admin.site.register(City, CityAdmin)
admin.site.register(Query, QueryAdmin)