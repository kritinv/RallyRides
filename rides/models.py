from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, default="")  # Added field
  email = models.EmailField(max_length=64, default="")  # Added field

  origination_state = models.CharField(max_length=2, default="") # Added field
  origination_city = models.CharField(max_length=64) # Updated to origination city
  destination_state = models.CharField(max_length=2)
  destination_city = models.CharField(max_length=64)

  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)

  vehicle_type = models.CharField(max_length=64, default="")  # Added field for vehicle type
  service_type = models.CharField(max_length=10, choices=[('regular', 'Regular CartyCity'), ('premium', 'Premium CartyCity')], default='regular')  # Added field for service type
