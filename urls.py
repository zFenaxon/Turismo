from django.urls import path
from .views import *

urlpatterns = [
	path('', index,name="index"),
	path('login/', login,name="login"),
	path('Test/', Test,name="Test"),
]