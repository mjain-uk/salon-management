from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    preferences = models.TextField()
    notes = models.TextField()
    join_date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username
