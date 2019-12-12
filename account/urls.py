from django.urls import path
from .views import register

app_name = "account"
urlpatterns = [
    path('', register, name = 'register'),
]