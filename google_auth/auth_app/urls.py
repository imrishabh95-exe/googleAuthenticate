from django.urls import path, include
from . import views

#http://127.0.0.1:8000/company/WIPRO.NS/
app_name = 'auth_app'
urlpatterns = [
    path('', views.home_page, name='home'),
]