from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),  # главная страница по адресу /
    path('contacts/', views.contacts, name='contacts'),  # страница контактов по адресу /contacts/
]
