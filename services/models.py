from django.db import models

# Create your models here.
class Service(models.Model):
    SERVICE_CATEGORIES = [
        ("HR", "Hair"),
        ("MK", "Makeup"),
        ("CS", "Custom")
    ]
    name = models.CharField(max_length=100, blank=False, unique=True)
    category = models.CharField(max_length=3, choices=SERVICE_CATEGORIES, blank=False, default="MK")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}-{self.get_category_display()}"
