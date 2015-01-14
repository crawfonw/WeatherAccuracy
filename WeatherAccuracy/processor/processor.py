from models import WeatherConditionCode, CurrentWeatherDatum
from tracker.models import Query

class WeatherProcessor():
    
    def __init__(self):
        pass
    
    def translate_queries(self):
        raise NotImplementedError

class CurrentWeatherProcessor(WeatherProcessor):
    def translate_():
        pass

    def process_current_weather_queries(_max=50):
        queries = Query.objects.order_by('time_executed').filter(query_type='C')
        return queries