from django.db import models
from datetime import datetime
# Create your models here.
class Vehicle(models.Model):
	vehicle_no=models.CharField(max_length=30)
	last_stoppage=models.CharField(max_length=30)
	current_position=models.CharField(max_length=30)
	distance_covered=models.IntegerField(default=0)
	last_updated=models.DateTimeField(default=datetime.now)
	vehicle_status=models.IntegerField(default=0)
	vehicle_name=models.CharField(max_length=100,default='BMW')
	name = models.CharField(max_length=50,default='Anuj')
	buy_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.vehicle_no

class Driver(models.Model):
	driver_name=models.CharField(max_length=40)
	gender=models.CharField(max_length=10)
	license_no=models.IntegerField()
	address=models.CharField(max_length=30)
	contact_no=models.BigIntegerField()
	license_expiry_date=models.DateField()
	vehicle_no = models.ForeignKey(Vehicle, on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.driver_name
