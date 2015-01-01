from django.db import models

class CurrentWeatherDatum(models.Model):
    city_id = models.IntegerField(help_text='From openweathermap')
    unix_date = models.IntegerField(help_text='Date when queried from API, in Unix time')
    name = models.CharField(max_length=100)
    
    coord_lat = models.DecimalField(help_text='City Latitude')
    coord_lon = models.DecimalField(help_text='City Longitude')
    
    sys_country = models.CharField(max_length=50)
    sys_sunrise = models.IntegerField(help_text='Unix sunrise time')
    sys_sunset = models.IntegerField(help_text='Unix sunset time')
    
    main_temp = None
    main_humidity = None
    main_temp_min = None
    main_temp_max = None
    main_pressure = None
    main_sea_level = None
    main_ground_level = None
    
    wind_speed = None
    wind_deg = None
    wind_gust = None
    
    clounds_all = None
    
    weather_id = None
    weather_main = None
    weather_description = None
    weather_icon_id = None
    
    rain_3h = None
    snow_3h = None
    
    class Meta:
        ordering = ('city_id',)
        verbose_name_plural = 'CurrentWeatherData'
    
    def __unicode__(self):
        return