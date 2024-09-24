from django.urls import path, include
from rest_framework import routers
from appointments.views import AppointmentView

router = routers.DefaultRouter()



urlpatterns = [path('appointments/', AppointmentView.as_view())]

urlpatterns+=router.urls
