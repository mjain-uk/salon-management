from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    preferences = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username
