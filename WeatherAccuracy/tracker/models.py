from django.db import models
from jsonfield import JSONField

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #query_string = models.CharField(max_length=100, required=False)
    city_id = models.IntegerField(help_text='City ID from openweathermap.')
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Cities'
    
    def __unicode__(self):
        return unicode(self.name)
    
class Query(models.Model):
    QUERY_TYPES = (('C', 'Current'),
                   ('D', 'Daily Forecast'),
                   ('H', 'Hourly Forecast'),
                   )
    
    city = models.ForeignKey(City)
    time_executed = models.DateTimeField()
    query_type = models.CharField(choices=QUERY_TYPES, max_length=8)
    full_query_string = models.CharField(max_length=500)
    raw_results = JSONField()
    was_success = models.NullBooleanField()
    
    class Meta:
        ordering = ('-time_executed', 'city',)
        verbose_name_plural = 'Queries'
    
    def __unicode__(self):
        return unicode(unicode(self.city) + ' at ' + unicode(self.time_executed))