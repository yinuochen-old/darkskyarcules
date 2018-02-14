import urllib.request, urllib.parse, urllib.error
import json
import datetime
import apikey

def getWeather(latitude,longitude):

    key = apikey.darkskykey
    print(datetime.datetime.now().timestamp())
    exclusions = 'minutely,hourly'

    days = list()
    tempHigh = list()
    tempLow = list()

    # loop through the seven days
    for day in range(0,7):
        time = datetime.datetime.utcnow() - datetime.timedelta(day)
        days.append(datetime.datetime.now().date()-datetime.timedelta(day))
        time = int(time.timestamp())

        # create api url
        urltime = darkskyparse(key,latitude,longitude,time,exclusions)
        print("Retrieving",urltime)

        try:
            uh = urllib.request.urlopen(urltime)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            break

        # decode to unicode
        data = uh.read().decode()

        try:
            # convert to json and load all days into an array
            js = json.loads(data)
        except:
            js = None

        tempHigh.append(js['daily']['data'][0]['temperatureHigh'])
        tempLow.append(js['daily']['data'][0]['temperatureLow'])
        #print("Temperature High", js['daily']['data'][0]['temperatureHigh'])
        #print("Temperature Low", js['daily']['data'][0]['temperatureLow'])

    return days, tempHigh, tempLow

def darkskyparse(key,latitude,longitude,time,exclusions=''):
    url = 'https://api.darksky.net/forecast/' + key + '/' + latitude + ',' + longitude + ',' + str(time)+'?' + urllib.parse.urlencode({'exclude': exclusions})
    return url
