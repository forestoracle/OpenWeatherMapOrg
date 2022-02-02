"""
API получения прогноза погоды с сайта openweathermap.org

    Account:   forest.oracle
      EMail:   forest.oracle@gmail.com
    API Key:   8e9b3d3c89bc21f854d16d22f45d8b65
    
    Санкт-Петербург ID = 498817
    Первомайск ID = 511002

    Примеры запросов:

      Запрос текущей погоды для Ленинграда в метрической системе.
        http://api.openweathermap.org/data/2.5/weather?id=498817&APPID=8e9b3d3c89bc21f854d16d22f45d8b65&units=metric
      
      Запрос текущей погоды для Ленинграда в метрической системе на русском языке.
        http://api.openweathermap.org/data/2.5/weather?id=498817&APPID=8e9b3d3c89bc21f854d16d22f45d8b65&units=metric&lang=ru
      
      Запрос погоды на 2 дня для Ленинграда в метрической системе на русском языке
        http://api.openweathermap.org/data/2.5/onecall?lon=30.26&lat=59.89&APPID=8e9b3d3c89bc21f854d16d22f45d8b65&units=metric&lang=ru
            
"""
import json
import urllib.parse
import urllib.request


class OpenWeatherMapOrg:
    def __init__(self, appid: str, units: str = 'metric', lang: str = 'en', mode: str = 'json'):
        """
        Конструктор
        """
        self.appid = appid
        self.units = units
        self.lang = lang
        self.mode = mode
        self.url = 'http://api.openweathermap.org/data/2.5/weather'
        self.params = {}

    def get_curr_weather_by_city(self, CityID: int = 498817):
        self.params = {'APPID': self.appid,
                       'units': self.units,
                       'lang': self.lang,
                       'mode': self.mode
                       }
        full_url = '{0}?{1}'.format(url, urllib.parse.urlencode(values))
        answer = urllib.request.urlopen(full_url)
        if answer.msg == 'OK':
            json_var = json.loads(str(answer.read(), "UTF-8"))


url = 'http://api.openweathermap.org/data/2.5/weather'
values = {'id': '498817',
          'APPID': '8e9b3d3c89bc21f854d16d22f45d8b65',
          'units': 'metric',
          'lang': 'en',
          'mode': 'json'}

data = urllib.parse.urlencode(values)
full_url = url + '?' + data
the_page = urllib.request.urlopen(full_url)

if the_page.msg == 'OK':
    js = the_page.read()

jstr = str(js, "UTF-8")

y = json.loads(jstr)

print("      Temperature: ", y["main"]["temp"], "C*")
print("Temperature (min): ", y["main"]["temp_min"], "C*")
print("Temperature (max): ", y["main"]["temp_max"], "C*")
print("       Feels like: ", y["main"]["feels_like"], "C*")
print("         Humidity: ", y["main"]["humidity"], "%")
print("         Pressure: ", y["main"]["pressure"], "Pa")
print("         Pressure: ", int(int(y["main"]["pressure"]) / 1.33), "")
