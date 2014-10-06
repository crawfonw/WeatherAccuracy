from django.contrib import admin
from models import City, Query

class FengShuiAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 50
    
class CityAdmin(FengShuiAdmin):
    list_display = ('name', 'query_string',)
    
class QueryAdmin(FengShuiAdmin):
    list_display = ('city', 'time_executed', 'full_query_string',)

admin.site.register(City, CityAdmin)
admin.site.register(Query, QueryAdmin)