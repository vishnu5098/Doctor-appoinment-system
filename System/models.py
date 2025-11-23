from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField(max_length=225)

    def __str__(self):
        return self.dep_name
     

 
class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    doc_name = models.CharField(max_length=225)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    avail_days = models.CharField(max_length=100, default="Monday")

    def __str__(self):
        return 'Dr ' + self.doc_name + ' (' + self.doc_spec + ')'

class Booking(models.Model):
    p_name=models.CharField(max_length=250)    
    p_phone=models.CharField(max_length=50,unique=True)
    p_email=models.EmailField(unique=True)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_datetime = models.DateTimeField(default=timezone.now)
    booked_on=models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.booking.p_name} - {self.status}"
        
