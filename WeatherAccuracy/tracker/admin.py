from django.contrib import admin

from WeatherAccuracy.shared_admin import FengShuiAdmin
from models import City, Query
    
class CityAdmin(FengShuiAdmin):
    list_display = ('name', 'city_id',)
    
class QueryAdmin(FengShuiAdmin):
    fieldsets = (
                  ('General Information', {
                          'fields': ('id', 'city', 'time_executed', 'query_type', 
                                     'full_query_string', 'was_success', 'picked_up_by_processor'),
                          }),
                  ('Query Results', {
                                     'classes': ('collapse', ),
                                     'fields': ('raw_results', ),
                                    }),
                  )
    
    list_display = ('city', 'time_executed', 'full_query_string', 
                    'query_type', 'was_success',)
    list_filter = ('query_type', 'was_success',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [x.name for x in obj._meta.fields]
        return self.readonly_fields
    
    def has_add_permission(self, request):
        return False

admin.site.register(City, CityAdmin)
admin.site.register(Query, QueryAdmin)