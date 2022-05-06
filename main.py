import requests 
import json 
ciudades={}
url:str="http://api.openweathermap.org/data/2.5/weather?"
ciudad=input("ciudad: ")
lon=float(input("longitud: "))
lat=float(input("latitud: "))
temp=float(input("temperatura: "))
arg={
    'nombre':ciudad,
    'longitud': lon,
    'latitud': lat,
    'temperatura': temp
}
response= requests.post(url,data=arg)
print(response.text) 
print("xxx")

