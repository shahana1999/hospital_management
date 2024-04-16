from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):#this class to show the booking details in a table on admin site
    list_display =('id','patient_name','phone','email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)