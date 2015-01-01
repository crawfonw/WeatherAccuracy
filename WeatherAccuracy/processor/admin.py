from django.contrib import admin

from WeatherAccuracy.shared_admin import FengShuiAdmin
from models import WeatherConditionCode, CurrentWeatherDatum

class WeatherConditionCodeAdmin(FengShuiAdmin):
    list_display = ('condition_id', 'main',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [x.name for x in obj._meta.fields]
        return self.readonly_fields

class CurrentWeatherDatumAdmin(FengShuiAdmin):
    fieldsets = (
                  ('General Information', {
                          'fields': ('raw_query', 'city_id', 'unix_date', #'id',
                                     'name', 'coord_lat', 'coord_lon',),
                          }),
                 ('Main', {
                         'classes': ('collapse', ),
                         'fields': ('weather_list', 'main_temp', 'main_humidity', 'main_temp_min',
                                    'main_temp_max', 'main_pressure', 'main_sea_level',
                                    'main_ground_level', 'wind_speed', 'wind_deg', 
                                    'wind_gust', 'clounds_all', 'rain_3h', 'snow_3h',),
                        }),
                  ('Sys', {
                         'classes': ('collapse', ),
                         'fields': ('sys_country', 'sys_sunrise', 'sys_sunset',),
                        }),
                  )
    
    list_display = ('unix_date', 'name', 'city_id',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [x.name for x in obj._meta.fields]
        return self.readonly_fields
    
    #def has_add_permission(self, request):
    #    return False

admin.site.register(WeatherConditionCode, WeatherConditionCodeAdmin)
admin.site.register(CurrentWeatherDatum, CurrentWeatherDatumAdmin)