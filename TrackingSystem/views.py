from django.shortcuts import render
from .models import Driver, Vehicle
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def index(request):
	all_vehicle= Vehicle.objects.all()
	all_driver = Driver.objects.all()
	values = []
	for i in all_vehicle:
		# print("--------------------------------", i)
		x = Driver.objects.get(vehicle_no=i)
		# print("------------:::::::::::::::::", x)
		values.append(x)
	# print("VALUES>>>>>>>>>>>>>>>>>>>>>>>>.", values)

	return render(request, 'TrackingSystem/index.html', {'all_driver':values})

 

def driverRegister(request):
	
	if request.method == 'POST':
		driver_name=request.POST['DriverName']
		license_no=request.POST['license_no']
		address=request.POST['address']
		contact_no=request.POST['Contact_no']
		license_expiry_date=request.POST['license_expiry_date']
		gender=request.POST['gender']
		gender='Male'
		#vehicle_no=Vehicle.objects.all()[0]
		Driver.objects.create(driver_name=driver_name,gender=gender,license_no=license_no,address=address,contact_no=contact_no
			,license_expiry_date=license_expiry_date)
		
		#redirect('TrackingSystem/index.html')
		return HttpResponseRedirect('/track/')
	else:
		return HttpResponseRedirect('/track/')

def driver_info(request):
	all_driver = Driver.objects.all()
	return render(request, 'TrackingSystem/Driver_info.html',{'all_driver':all_driver})

def vehicle_info(request):
	all_vehicle=Vehicle.objects.all()
	return render(request,'TrackingSystem/Vehicle_info.html',{'all_vehicle':all_vehicle})