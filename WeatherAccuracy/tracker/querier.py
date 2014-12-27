import urllib2, urllib, json

CURRENT_WEATHER = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric'
HOURLY_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&units=metric' #every 3 hours for 5 days ahead
SIXTEEN_DAY_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast/daily?id=%s&units=metric&cnt=16' #daily up to 16 days in the future

def _query_api(url, city_id):
    query_url = url % city_id
    result = urllib2.urlopen(query_url).read()
    data = json.loads(result)
    return query_url, data

def current_weather_for(city_id):
    return _query_api(CURRENT_WEATHER, city_id)

def five_day_weather_for(city_id):
    return _query_api(HOURLY_FORECAST, city_id)

def sixteen_day_weather_for(city_id):
    return _query_api(SIXTEEN_DAY_FORECAST, city_id)