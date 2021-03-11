import requests

try:
	city = input("Enter city name --> ")
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 =  "&appid="+"c6e315d09197cec231495138183954bd"
	wa = a1 + a2 + a3
		
	res = requests.get(wa)
	print(res)
	
	data = res.json()
	print(data)
	
	temp =  data['main']['temp']
	print("Tempreature = ", temp)
	
	desc = data['weather'][0]['description']	
	print("Weather description = ",desc)
except Exception as e:
	print("Issue -->",e)