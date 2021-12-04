import requests
import json

### TODO:
### 1. Automate api call (daily @ 12:01)
### 2. Handle cases for each data point
### 3. Determine injection format.  
###        List(len = 24) -> one per hour
###          <List(len = 3) -> temp, wind, weather description
###             <light state>>>


# url args
latitude = '49.70'
longitude = '-123.14'
apiKey = 'd29f5764c1985aa8462a589923819331'

hourlyWeatherUrl = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&units=metric&exclude=current,minutely,daily,alerts&appid={apiKey}'

weatherRes = requests.get(hourlyWeatherUrl)
weatherDataObject = json.loads(weatherRes.content)


dayTempsList = []
dayWeatherList = []  #https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
dayWindSpeedList = []

# Gets data for each hour of the day (starts at 00:00)
for i in range(24):
    dayTempsList.append(weatherDataObject['hourly'][i]['temp'])
    dayWeatherList.append(weatherDataObject['hourly'][i]['weather'][0]['description'])
    dayWindSpeedList.append(weatherDataObject['hourly'][i]['wind_speed'])

## Handles Temperatures
## Colored
for temp in dayTempsList:
    if temp < -30:
        print(temp)
    elif temp < -20:
        print(temp)
    elif temp < -10:
        print(temp)
    elif temp < -5:
        print(temp)
    elif temp < 0:
        print(temp)
    elif temp < 5:
        print(temp)
    elif temp < 10:
        print(temp)
    elif temp < 15:
        print(temp)
    elif temp < 20:
        print(temp)
    elif temp < 25:
        print(temp)
    elif temp < 30:
        print(temp)
    elif temp < 35:
        print(temp)
    elif temp < 40:
        print(temp)
    elif temp < 45:
        print(temp)
    elif temp < 50:
        print(temp)
    else:
        print('HOLY FUCK IT IS HOT')

## Handles Weather Descriptions
for weatherDescription in dayWeatherList:
    # THUNDERSTORM
    if weatherDescription == 'thunderstorm with light rain':
        print(weatherDescription)
    if weatherDescription == 'thunderstorm with rain':
            print(weatherDescription)
    if weatherDescription == 'thunderstorm with heavy rain':
            print(weatherDescription)
    if weatherDescription == 'light thunderstorm':
            print(weatherDescription)
    if weatherDescription == 'thunderstorm':
            print(weatherDescription)
    if weatherDescription == 'heavy thunderstorm':
            print(weatherDescription)
    if weatherDescription == 'ragged thunderstorm':
            print(weatherDescription)
    if weatherDescription == 'thunderstorm with light drizzle':
            print(weatherDescription)
    if weatherDescription == 'thunderstorm with drizzle':
            print(weatherDescription)
    if weatherDescription == 'thunderstorm with heavy drizzle':
            print(weatherDescription)

    # DRIZZLE
    if weatherDescription == 'light intensity drizzle':
            print(weatherDescription)
    if weatherDescription == 'drizzle':
            print(weatherDescription)
    if weatherDescription == 'heavy intensity drizzle':
            print(weatherDescription)
    if weatherDescription == 'light intensity drizzle rain':
            print(weatherDescription)
    if weatherDescription == 'drizzle rain':
            print(weatherDescription)
    if weatherDescription == 'heavy intensity drizzle rain':
            print(weatherDescription)
    if weatherDescription == 'shower rain and drizzle':
            print(weatherDescription)
    if weatherDescription == 'heavy shower rain and drizzle':
            print(weatherDescription)
    if weatherDescription == 'shower drizzle':
            print(weatherDescription)
    # RAIN
    if weatherDescription == 'light rain':
            print(weatherDescription)
    if weatherDescription == 'moderate rain':
            print(weatherDescription)
    if weatherDescription == 'heavy intensity rain':
            print(weatherDescription)
    if weatherDescription == 'very heavy rain':
            print(weatherDescription)
    if weatherDescription == 'extreme rain':
            print(weatherDescription)
    if weatherDescription == 'freezing rain':
            print(weatherDescription)
    if weatherDescription == 'light intensity shower rain':
            print(weatherDescription)
    if weatherDescription == 'shower rain':
            print(weatherDescription)
    if weatherDescription == 'heavy intensity shower rain':
            print(weatherDescription)
    if weatherDescription == 'ragged shower rain':
            print(weatherDescription)
    # SNOW
    if weatherDescription == 'light snow':
            print(weatherDescription)
    if weatherDescription == 'Snow':
            print(weatherDescription)
    if weatherDescription == 'Heavy snow':
            print(weatherDescription)
    if weatherDescription == 'Sleet':
            print(weatherDescription)
    if weatherDescription == 'Light shower sleet':
            print(weatherDescription)
    if weatherDescription == 'Shower sleet':
            print(weatherDescription)
    if weatherDescription == 'Light rain and snow':
            print(weatherDescription)
    if weatherDescription == 'Rain and snow':
            print(weatherDescription)
    if weatherDescription == 'Light shower snow':
            print(weatherDescription)
    if weatherDescription == 'Shower snow':
            print(weatherDescription)
    if weatherDescription == 'Heavy shower snow':
            print(weatherDescription)
    # MISC
    if weatherDescription == 'mist':
            print(weatherDescription)
    if weatherDescription == 'Smoke':
            print(weatherDescription)
    if weatherDescription == 'Haze':
            print(weatherDescription)
    if weatherDescription == 'sand/ dust whirls':
            print(weatherDescription)
    if weatherDescription == 'fog':
            print(weatherDescription)
    if weatherDescription == 'sand':
            print(weatherDescription)
    if weatherDescription == 'dust':
            print(weatherDescription)
    if weatherDescription == 'volcanic ash':
            print(weatherDescription)
    if weatherDescription == 'squalls':
            print(weatherDescription)
    if weatherDescription == 'tornado':
            print(weatherDescription)
    # CLEAR SKY
    if weatherDescription == 'clear sky':
            print(weatherDescription)
    # CLOUDS
    if weatherDescription == 'few clouds':
            print(weatherDescription)
    if weatherDescription == 'scattered clouds':
            print(weatherDescription)
    if weatherDescription == 'broken clouds':
            print(weatherDescription)
    if weatherDescription == 'overcast clouds':
            print(weatherDescription)


## Handles Wind Speed
for windSpeed in dayWindSpeedList:
    if windSpeed == 0:
        print(windSpeed)
    elif windSpeed < 5:
        print(windSpeed)
    elif windSpeed < 10:
        print(windSpeed)
    elif windSpeed < 15:
        print(windSpeed)
    elif windSpeed < 20:
        print(windSpeed)
    elif windSpeed < 25:
        print(windSpeed)
    elif windSpeed < 30:
        print(windSpeed)
    elif windSpeed < 35:
        print(windSpeed)
    elif windSpeed < 40:
        print(windSpeed)
    elif windSpeed < 45:
        print(windSpeed)
    elif windSpeed < 50:
        print(windSpeed)
    elif windSpeed < 55:
        print(windSpeed)
    elif windSpeed < 60:
        print(windSpeed)
    elif windSpeed < 65:
        print(windSpeed)
    elif windSpeed < 70:
        print(windSpeed)
    elif windSpeed < 75:
        print(windSpeed)
    elif windSpeed < 55:
        print('IT IS FUCKING WINDY')





