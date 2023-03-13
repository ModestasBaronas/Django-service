from django import forms
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils import timezone

from .models import Appointment, Car, Customer


class AppointmentStepOneForm(forms.ModelForm):
    date = forms.DateField(initial=timezone.now().date(), widget=forms.SelectDateWidget())
    time = forms.ChoiceField(choices=Appointment.times)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'name', 'email', 'phone_number']


class AppointmentStepTwoForm(forms.ModelForm):
    year = forms.ChoiceField(choices=Car.YEAR_CHOICES)
    engine_type = forms.ChoiceField(choices=Car.ENGINE_TYPE_CHOICES)
    make = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    engine_displacement = forms.FloatField()
    engine_power_kw = forms.FloatField()

    class Meta:
        model = Car
        fields = ['year', 'engine_type', 'make', 'model', 'engine_displacement', 'engine_power_kw']










# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from .models import Customer, Calendar, Car
#
#
# class AppointmentStep1Form(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=20)
#     date = forms.ModelChoiceField(queryset=Calendar.objects.filter(is_available=True), empty_label=None)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Next'))
#         self.helper.layout = Layout(
#             Field('name', placeholder='Your name'),
#             Field('email', placeholder='Your email'),
#             Field('phone_number', placeholder='Your phone number'),
#             Field('date', css_class='datepicker')
#         )
#
# class AppointmentStep2Form(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ['year', 'engine_type', 'make', 'model', 'engine_displacement', 'engine_power_kw']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Create Appointment'))
#         self.helper.layout = Layout(
#             Field('year', css_class='form-control'),
#             Field('engine_type', css_class='form-control'),
#             Field('make', css_class='form-control'),
#             Field('model', css_class='form-control'),
#             Field('engine_displacement', css_class='form-control'),
#             Field('engine_power_kw', css_class='form-control')
#         )