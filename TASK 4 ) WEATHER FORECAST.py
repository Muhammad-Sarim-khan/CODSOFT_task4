#importing necessary libraries
from tkinter import *
import requests
from PIL import ImageTk,Image
import tkinter as tk

#creating main window
root=Tk()
root.geometry("645x645")

#setting window icon
root.iconphoto(False,tk.PhotoImage(file="weather_icon.png") )

#url and api to get weather data
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key="f293b4c8649fbe9f9f5b73175aa78e97"

#sorting data from dictionary
def sort_weather():
    city_name=e1.get()
    get_weather=requests.get(url.format(city_name,api_key))
    json=get_weather.json()
    print(json)
    city=json['name']
    country=json['sys']['country']
    temperature=json['main']['temp']
    temperature_in_celsius=round(temperature-273.15,1)
    weather=json['weather'][0]['description']
    humidity=json['main']['humidity']
    wind_speed=json['wind']['speed']

    #updating labels to display the information of weather
    l3.config(text="Country: " + country,font="helvetica 13 bold")
    l4.config(text="City: " + city,font="helvetica 13 bold")
    l5.config(text="Temperature: " + str(temperature_in_celsius) + "°C",font="helvetica 13 bold")
    l6.config(text="Humidity: " + str(humidity) + "%",font="helvetica 13 bold")
    l7.config(text="Wind Speed: " + str(wind_speed) + " m/s",font="helvetica 13 bold")
    l8.config(text="Weather Description: " + weather,font="helvetica 13 bold")

root.title("WEATHER FORECAST APPLICATION")
l1=Label(root,text="WEATHER FORECAST",font="times 28 bold",fg="royalblue4")
l1.place(x=155,y=38)
l2=Label(root,text="CITY : ",font="helvetica 18 bold")
l2.place(x=160,y=160)

#labels to display information as text
l3=Label(root,text="")
l3.place(x=287,y=320)
l4=Label(root,text="")
l4.place(x=287,y=370)
l5=Label(root,text="")
l5.place(x=260,y=420)
l6=Label(root,text="")
l6.place(x=287,y=470)
l7=Label(root,text="")
l7.place(x=258,y=520)
l8=Label(root,text="")
l8.place(x=208,y=570)

#creating an entry to get the city name from user
e1=Entry(root,width=30,font="helvetica 11 bold")
e1.place(x=250,y=167)

#button to get the weather information of the entered city
b1=Button(root,text="GET WEATHER",command=sort_weather,pady=10,padx=10,font="helvetica 11 bold",bg="gold1",fg="black",borderwidth=2,cursor="hand2")
b1.place(x=270,y=230)

#diplaying an image in the window
image = Image.open("weather.png")
image = image.resize((80, 80))
weather_image = ImageTk.PhotoImage(image)
l9 = Label(image=weather_image)
l9.place(x=40,y=20)

mainloop()