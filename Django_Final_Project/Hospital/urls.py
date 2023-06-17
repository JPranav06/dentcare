from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('appointment', views.appointment),
    path('service', views.service),
    path('price', views.price),
    path('team', views.team),
    path('contact', views.contact),
    path('testimonial', views.testimonial),
    path('about', views.about),
    path('success', views.success),
    path('list', views.appointmentlist, name='appointmentDetails'),
    path('add', views.appointmentAdd, name='appointmentConfirm'),
]
