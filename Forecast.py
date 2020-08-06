# Date:         10/07/2020
# Version:      Python 3.8

# This class represents a complete weather forecast
# This class is implemented by creating a list of the Weather object

from Weather import Weather
from datetime import datetime
import calendar


class Forecast:

    # Constants
    CURRENT_DAY_NUMBER = datetime.today().weekday()
    LIST_SIZE = 4
    WEEK_DAYS = 7

    def __init__(self, data, city):
        self.forecast = self.__create_forecast(data, city)
        self.city = city.capitalize()

    def __create_forecast(self, data, city):
        forecast = []
        for i in range(Forecast.LIST_SIZE):      # i indicates the number of days from the current day
            d = calendar.day_name[(Forecast.CURRENT_DAY_NUMBER + i) % Forecast.WEEK_DAYS]        # Uses modulus because the numbers range from 0 -6 representing the days
            forecast.append(Weather(data, city, d, i))
        return forecast


