from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.mail import send_mail


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    YEAR_CHOICES = [(str(i), str(i)) for i in range(1960, timezone.now().year + 1)]
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    ENGINE_TYPE_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('petrol_lpg', 'Petrol/LPG'),
    ]
    engine_type = models.CharField(max_length=100, choices=ENGINE_TYPE_CHOICES)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine_displacement = models.FloatField()
    engine_power_kw = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.engine_type})"


class Appointment(models.Model):
    times = (
        (9, '9:00 AM'),
        (12, '12:00 PM'),
        (15, '3:00 PM'),
    )
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    date = models.DateField(default=timezone.now)
    time = models.IntegerField(choices=times, default=9)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered', editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.time} - {self.customer.name}"

    # def approve(self):
    #     self.status = 'approved'
    #     self.save()
    #     send_mail(
    #         'Appointment Approved',
    #         f'Your appointment on {self.date} at {self.time} has been approved.',
    #         'from@example.com',
    #         [self.customer.email],
    #         fail_silently=False,
    #     )

