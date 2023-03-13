from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_appointment/', views.make_appointment_step_one, name='make_appointment_step_one'),
    path('make_appointment/step_two/', views.make_appointment_step_two, name='make_appointment_step_two'),
    path('make_appointment/success/', views.appointment_success, name='appointment_success'),
]
