# Date:         10/07/2020
# Version:      Python 3.8

from tkinter import *
from PIL import ImageTk, Image


class ResultWindow:

    def __init__(self, forecast):
        self.window = Toplevel()
        self.canvas = Canvas(self.window, height=600, width=300)
        self.__fill_window(forecast)

    # Fills the window with everything
    def __fill_window(self, forecast):
        self.__set_window_settings()
        self.__set_background(forecast)
        self.__create_top(forecast.city)
        self.__show_temp(forecast)
        self.__show_stats(forecast)
        self.__show_forecast(forecast)
        self.__show_credits()

    # Sets the basic window settings
    def __set_window_settings(self):
        self.window.title('Weather Report')
        self.window.iconbitmap('media/weather.ico')
        self.window.geometry('300x600')
        self.window.resizable(False, False)         # Makes the window size constant

    # Creates the top part of the window
    def __create_top(self, city):
        self.canvas.create_text(150, 60, fill='white', text=city, font=('david', 25, 'bold'))

    def __show_temp(self, forecast):
        self.canvas.create_text(150, 125, fill='white', text=forecast.forecast[0].current_temp, font=('arial', 25, 'bold'))
        self.canvas.create_text(150, 150, fill='white', text=forecast.forecast[0].weather, font=('comic sans ms', 10))

    def __set_background(self, forecast):
        # Grabs the fitting image from the backgrounds folder according to the weather
        global image        # Global just so it won't be garbage collected
        path = self.__get_picture(forecast)
        image = ImageTk.PhotoImage(Image.open(path))

        # Displays the image on a canvas which covers the whole window
        self.canvas.create_image(300, 600, image=image)
        self.canvas.place(relwidth=1, relheight=1)

    # Shows the stats on the current day
    def __show_stats(self, forecast):
        self.canvas.create_text(3, 200, anchor=W, fill='white', text=f'Humidity: {forecast.forecast[0].humidity}', font=('comic sans ms', 10, 'bold'))
        self.canvas.create_text(3, 225, anchor=W, fill='white', text=f'Max temperature: {forecast.forecast[0].max_temp}', font=('comic sans ms', 10, 'bold'))
        self.canvas.create_text(3, 250, anchor=W, fill='white', text=f'Min temperature: {forecast.forecast[0].min_temp}', font=('comic sans ms', 10, 'bold'))
        self.canvas.create_text(3, 275, anchor=W, fill='white', text=f'Wind speed: {forecast.forecast[0].wind_speed}', font=('comic sans ms', 10, 'bold'))

    # Shows some stats on the next 3 days
    def __show_forecast(self, forecast):
        self.canvas.create_text(3, 350, anchor=W, fill='white', text=f'{forecast.forecast[1].day}\t\t    {forecast.forecast[1].max_temp}   {forecast.forecast[1].min_temp}', font=('comic sans ms', 10, 'bold'))
        self.canvas.create_text(3, 375, anchor=W, fill='white', text=f'{forecast.forecast[2].day}\t\t\t    {forecast.forecast[2].max_temp}   {forecast.forecast[2].min_temp}', font=('comic sans ms', 10, 'bold'))
        self.canvas.create_text(3, 400, anchor=W, fill='white', text=f'{forecast.forecast[3].day}\t\t\t    {forecast.forecast[3].max_temp}   {forecast.forecast[3].min_temp}', font=('comic sans ms', 10, 'bold'))

    # Shows the source of the data
    def __show_credits(self):
        self.canvas.create_text(25, 550, anchor=W, fill='white', text='All data came from OpenWeather API', font=('arial', 10, 'bold'))

    # Returns the correct path to the background picture needed according to the weather description
    def __get_picture(self, forecast):
        description = forecast.forecast[0].weather
        folder_path = 'media\\backgrounds\\'
        if 'cloud' in description:
            return folder_path + 'cloudy_day.jpg'
        elif 'rain' in description:
            return folder_path + 'rainy_day.jpg'
        else:
            return folder_path + 'clear_day.jpg'
