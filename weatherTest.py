import urllib2, urllib, json
#base_url = 'http://api.openweathermap.org/data/2.5/weather?'
base_url = 'http://api.openweathermap.org/data/2.5/forecast/city?'
query = 'London,uk'

query_url = base_url + 'q=' + query
result = urllib2.urlopen(query_url).read()
data = json.loads(result)
print data