import pyowm

def Weather():
	Location=input("Enter current location :")
	owm = pyowm.OWM('ed30c45f73d7d6dadde755cb0415c76e')
	observation = owm.weather_at_place(Location)
	w = observation.get_weather()
 
	print(w.get_wind())
	print(w.get_humidity())

Weather()
