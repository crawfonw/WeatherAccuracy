from django.db import models
from tracker.models import Query

class WeatherConditionCode(models.Model):
    condition_id = models.IntegerField(help_text='Weather condition id')
    main = models.CharField(max_length=100, help_text='Group of weather parameters (Rain, Snow, Extreme etc.)')
    description = models.CharField(max_length=100, help_text='Weather condition within the group')
    icon_id = models.CharField(max_length=100, help_text='Weather icon id')
    
    class Meta:
        ordering = ('condition_id',)
        
    def __unicode__(self):
        return unicode(self.main)

class CurrentWeatherDatum(models.Model):
    raw_query = models.ForeignKey(Query)
    city_id = models.IntegerField(help_text='City identification')
    unix_date = models.IntegerField(help_text='Data receiving time, unix time, GMT')
    name = models.CharField(max_length=100, help_text='City name')
    
    coord_lat = models.DecimalField(help_text='City geo location, latitude', decimal_places=5, max_digits=100)
    coord_lon = models.DecimalField(help_text='City geo location, longitude', decimal_places=5, max_digits=100)
    
    sys_country = models.CharField(max_length=50, help_text='Country (GB, JP etc.)')
    sys_sunrise = models.IntegerField(help_text='Sunrise time, unix, UTC')
    sys_sunset = models.IntegerField(help_text='Sunset time, unix, UTC')
    
    main_temp = models.DecimalField(help_text='Temperature, Kelvin (subtract 273.15 to convert to Celsius)', decimal_places=5, max_digits=100)
    main_humidity = models.DecimalField(help_text='Humidity, %', decimal_places=5, max_digits=100)
    main_temp_min = models.DecimalField(help_text='Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally)', decimal_places=5, max_digits=100)
    main_temp_max = models.DecimalField(help_text='Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally)', decimal_places=5, max_digits=100)
    main_pressure = models.DecimalField(help_text='Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa', decimal_places=5, max_digits=100)
    main_sea_level = models.DecimalField(help_text='Atmospheric pressure on the sea level, hPa', decimal_places=5, max_digits=100)
    main_ground_level = models.DecimalField(help_text='Atmospheric pressure on the ground level, hPa', decimal_places=5, max_digits=100)
    
    wind_speed = models.DecimalField(help_text='Wind speed, mps', decimal_places=5, max_digits=100)
    wind_deg = models.DecimalField(help_text='Wind direction, degrees (meteorological)', decimal_places=5, max_digits=100)
    wind_gust = models.DecimalField(help_text='Wind gust, mps', decimal_places=5, max_digits=100)
    
    clounds_all = models.DecimalField(help_text='Cloudiness, %', decimal_places=5, max_digits=100)
    
    weather_list = models.ManyToManyField(WeatherConditionCode)
    
    rain_3h = models.DecimalField(help_text='Precipitation volume for last 3 hours, mm', decimal_places=5, max_digits=100)
    snow_3h = models.DecimalField(help_text='Snow volume for last 3 hours, mm', decimal_places=5, max_digits=100)
    
    class Meta:
        ordering = ('city_id',)
        verbose_name_plural = 'Current Weather Data'
    
    def __unicode__(self):
        return