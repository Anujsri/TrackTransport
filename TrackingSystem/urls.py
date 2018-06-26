from django.conf.urls import url
from . import views
app_name= 'track'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^registerDriver/$', views.driverRegister, name='index1'),
	url(r'^driver_info/$', views.driver_info, name='driver_info'),
	url(r'^vehicle_info/$', views.vehicle_info, name='vehicle_info'),
]
