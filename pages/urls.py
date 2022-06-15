from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('about/',about_page,name='about'),
    path('services/',services_page,name='services'),
    path('contact/',contact_page,name='contact'),
]