from django.shortcuts import render
import requests

def home(request):
	if request.method =="POST":
		try:
			city = request.POST.get("city")
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city
			a3 =  "&appid="+"c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3
		
			res = requests.get(wa)
			data = res.json()
			temp =  data['main']['temp']
			desc = data['weather'][0]['description']	
			icon_add = "http://openweathermap.org/img/w/" + data['weather'][0]['icon']  + ".png"
			msg = "City name = " + str(city) + " 	Temp = " + str(temp) + " Des = " + str(desc)
			return render(request,"home.html",{'msg':msg,'icon':icon_add})
		except Exception as e:
			return render(request,"home.html",{'msg':'Check city name'})

	else:
		return render (request,'home.html')