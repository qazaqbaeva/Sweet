from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/',contact,name='contact'),
path('category/',category,name='category'),
path('single/',single,name='single'),

]