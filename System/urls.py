from django.urls import path
from.views import *
urlpatterns = [
    path('',index,name='home'),
    path('booking/',booking,name='booking'),
    path('doctors/',doctors,name='doctors'),
    path('department/',department,name='department'),
    path('status/',status_view,name='status'),
    path('contact',contact,name='contact'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view ,name='register'),
    path('doctorlogin/',doctor_login,name='doctorlogin'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('approve/<int:id>/', approve_booking, name='approve'),
    path('cancel/<int:id>/', cancel_booking, name='cancel'),


]
