from django.shortcuts import render, redirect
from .models import *


def appointmentlist(request):
    userdata = appointmentDetails.objects.all()
    return render(request, "list.html", {'userdata': userdata})


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def price(request):
    return render(request, 'price.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')


def appointment(request):
    return render(request, 'appointment.html')


def appointmentAdd(request):
    service = request.POST.get('service')
    doctor = request.POST.get('doctor')
    name = request.POST.get('name')
    email = request.POST.get('email')
    date1 = request.POST.get('date1')
    # time1 = request.POST.get('time1')
    appointmentDetails.objects.create(service=service, doctor=doctor, name=name, email=email, date1=date1).save()
    return redirect('/success')


def success(request):
    return render(request, 'success.html')
