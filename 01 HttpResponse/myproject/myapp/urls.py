from django.urls import path
from .views import display, myview, greeting

urlpatterns = [
    path('display/', display, name='display'),
    path('myview/', myview, name='myview'),
    path('greeting/', greeting, name='greeting'),
]
