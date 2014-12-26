from django.contrib import admin
from models import City, Query

class FengShuiAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 50
    
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