from django.contrib import admin
from diseases.models import Diseases,CustomUser,Booking,Routine
# Register your models here.
admin.site.register(Diseases)
admin.site.register(CustomUser)
admin.site.register(Booking)
admin.site.register(Routine)