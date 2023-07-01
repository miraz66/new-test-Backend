from django.urls import path
from . import views


urlpatterns = [
    path('api/customers/', views.Customers, name="customers"),
]
