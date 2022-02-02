from django.urls import path
from apidata import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>/',views.updating , name="updating"),
]