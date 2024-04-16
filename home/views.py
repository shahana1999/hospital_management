from django.shortcuts import render
from django.http import HttpResponse 
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.
def index(request):
   numbers = {
       'num1':[1,2,3,4,5,6,7,8,9,10]
   }
   return render(request,'index.html',numbers)
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    dict_form = {
        'form':BookingForm()
    }

    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_docs ={
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept = {
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
