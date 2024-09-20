from django.db import models
from clients.models import Client
from services.models import Service
from datetime import timedelta, date

# Create your models here.
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    event_date = models.DateField(blank=False)
    consultation_date = models.DateField(blank=True)
    notes = models.TextField(blank = True)
    estimated_total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)    

    def __str__(self):
        return f"{self.client.first_name}-{self.event_date}"
    
    def save(self, *args, **kwargs):
        today = date.today()
        if (self.event_date - today).days < 2:
            # If event date is less than 2 days from today, consultation date is tomorrow
            self.consultation_date = today + timedelta(days=1)
        else:
            # Otherwise, consultation date is 2 days from today
            self.consultation_date = today + timedelta(days=2)
        # Call the original save method
        super(Appointment, self).save(*args, **kwargs) 


