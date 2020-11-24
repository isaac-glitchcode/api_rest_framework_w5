from django.urls import path
from classes.views import get_classes, get_class

urlpatterns = [
    path('', get_classes ),
    path('class/<id>/', get_class)
    
]
