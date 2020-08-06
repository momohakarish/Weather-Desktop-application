# Date:         10/07/2020
# Version:      Python 3.8

# This class represents the weather for a certain day
# The data for the constructor is given in the form of a json file which is used to extract the data
# The data for the file is from the Open Weather API
# The specific API query is the "one call" request


class Weather:

    # ------------- Constants -------------
    DEGREE_SYMBOL = '°'
    WIND_SPEED_MEASUREMENT = 'm/s'

    def __init__(self, data, city, day, num):       # num represents the number of days from thd current day
        self.city = city.capitalize()       # Capitalizing the first letter as it is a name
        self.day = day
        self.current_temp = str(round(data['daily'][num]['temp']['day'])) + Weather.DEGREE_SYMBOL
        self.min_temp = str(round(data['daily'][num]['temp']['min'])) + Weather.DEGREE_SYMBOL
        self.max_temp = str(round(data['daily'][num]['temp']['max'])) + Weather.DEGREE_SYMBOL
        self.humidity = str(data['daily'][num]['humidity']) + '%'
        self.weather = data['daily'][num]['weather'][0]['description']
        self.wind_speed = str(round(data['daily'][num]['wind_speed'])) + Weather.WIND_SPEED_MEASUREMENT

    def __repr__(self):
        return f'City: {self.city}, Day: {self.day} , Wind speed: {self.wind_speed}, Humidity: {self.humidity}, Current temp: {self.current_temp}, Min temp: {self.min_temp}, Max temp: {self.max_temp}, Weather: {self.weather}'


