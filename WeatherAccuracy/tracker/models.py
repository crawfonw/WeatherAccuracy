from django.db import models
from jsonfield import JSONField

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    picked_up_by_processor = models.NullBooleanField(default=False)
    
    class Meta:
        ordering = ('-time_executed', 'city',)
        verbose_name_plural = 'Queries'
    
    def __unicode__(self):
        return unicode('%s at %s (%s)' % (unicode(self.city), unicode(self.time_executed), \
                                          dict(self.QUERY_TYPES).get(self.query_type)))