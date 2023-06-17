from django.db import models

class appointmentDetails(models.Model):
    service = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    date1 = models.DateField()

    def __str__(self):
        return self.name
