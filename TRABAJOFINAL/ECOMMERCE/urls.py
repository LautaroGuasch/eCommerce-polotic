from django.urls import path
from . import views

app_name = "ECOMMERCE"

urlpatterns = [
    path('', views.index, name="index")
]