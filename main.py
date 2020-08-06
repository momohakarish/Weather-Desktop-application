# Date:         10/07/2020
# Version:      Python 3.8

import requests
from ResultWindow import ResultWindow
from Forecast import Forecast
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# ------------- Files -------------
key_file = open('api.txt', 'r')


# ------------- Constants -------------
WEATHER_API_KEY = key_file.read().strip('\n')
DEFAULT_SEARCH_BAR_PROMPT = 'Enter city'
HTTP_FORMAT = 'http://'
UNITS = 'units=metric'


# ------------- Closing files -------------
key_file.close()

# ------------- Functions -------------


def search(*args):
    # Checks if the button was pressed when no city was entered
    if search_bar.get() == DEFAULT_SEARCH_BAR_PROMPT:
        messagebox.showerror('Error', 'Please enter a city name')
        return

    # Getting the city from the user and the coordinates for it using the weather API
    city = location.get()           # Getting the location from our global tkinter string variable
    url = f'{HTTP_FORMAT}api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&{UNITS}'
    coordinates = get_coordinates(url)

    if coordinates is None or return_forecast(coordinates, city) is None:         # Checks if the coordinates data is valid and the city data was found AKA not null
        messagebox.showerror('Error', 'Invalid city please enter another one')
        return

    forecast = return_forecast(coordinates, city)       # Create the forecast object for the result window
    ResultWindow(forecast)      # Display the window


# Returns a dictionary with the lat and lon coordinates of the city given in the url
def get_coordinates(url):
    # Calling the API to get coordinates for another API call
    result = requests.get(url)
    data = result.json()

    if not result.ok:  # Checks if we got a good http header response or an error one
        return None

    # Getting the coordinates for our city
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    return {'lat': lat, 'lon': lon}


# Returns a forecast object from coordinates and city name
def return_forecast(coordinates, city):
    # Extracting our coordinates
    lon = coordinates['lon']
    lat = coordinates['lat']

    # Getting the weather forecast for our city
    exclude = ['current', 'minutely', 'hourly']  # Excluding data we don't want from our API request
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&{UNITS}&appid={WEATHER_API_KEY}'
    result = requests.get(url)
    data = result.json()

    if not result.ok:
        return None

    return Forecast(data, city)


def display_weather():
    pass


# Clears the input field and puts the user's cursor on it
def clear_field():
    location.set('')
    search_bar.focus()

# ------------- Main code -------------


# Creating the main window
root = Tk()
root.title('Weather forecast')
root.iconbitmap('media/weather.ico')
root.geometry('600x450')
root.bind('<Return>', search)


# tkinter variables
location = StringVar()

# Input fields
search_bar = Entry(root, textvariable=location)
search_bar.insert(0, DEFAULT_SEARCH_BAR_PROMPT)
search_bar.focus()          # Makes the user's cursor default to the text entry widget


# Buttons
search_button = Button(root, text='Search', width=19, command=search)
clear_button = Button(root, text='Clear', width=19, command=clear_field)


# Displaying widgets
search_bar.grid(row=0, column=0)
search_button.grid(row=1, column=0)
clear_button.grid(row=2, column=0)


root.mainloop()