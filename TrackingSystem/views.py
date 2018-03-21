from django.shortcuts import render
from .models import Driver, Vehicle
# Create your views here.
def index(request):
	all_vehicle= Vehicle.objects.all()
	all_driver = Driver.objects.all()
	values = []
	for i in all_vehicle:
		# print("--------------------------------", i)
		x = Driver.objects.all().filter(vehicle_no=i).first()
		# print("------------:::::::::::::::::", x)
		values.append(x)
	# print("VALUES>>>>>>>>>>>>>>>>>>>>>>>>.", values)

	return render(request, 'TrackingSystem/index.html', {'all_driver':values})

 

