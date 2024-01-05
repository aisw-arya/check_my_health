from django.db import models
from django.contrib.auth.models import AbstractUser
import django

# Create your models here.
class Diseases(models.Model):
    disease=models.CharField(max_length=500)
    symptoms=models.CharField(max_length=1000)
    details=models.CharField(max_length=500)
    doctor=models.CharField(max_length=50)
    hospital=models.CharField(max_length=50)


    def __str__(self):
        return self.disease


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=200)
    image=models.ImageField(upload_to='diseases/photo',null=True,blank=True)

    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)

class Booking(models.Model):
    name = models.CharField(max_length=500)
    age=models.IntegerField()
    address=models.CharField(max_length=2000)
    phone=models.IntegerField()
    booking_date=models.DateTimeField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Routine(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    cholesterol=models.CharField(max_length=500)
    sugar=models.CharField(max_length=500)
    pressure=models.CharField(max_length=500)
    suggested = models.CharField(max_length=500)
    date_added=models.DateTimeField(auto_now_add=True)
