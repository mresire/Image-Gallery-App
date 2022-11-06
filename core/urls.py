from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('signup/',signup, name='signup'),
    path('upload/',upload, name='upload'),
    
]

