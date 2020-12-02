from django.urls import path
from professors.views import ListProfessorsAPIView, UpdateProfessorAPIView

urlpatterns = [
    path('', ListProfessorsAPIView.as_view(), name='professors'),
    path('<pk>/', UpdateProfessorAPIView.as_view(), name='professor'),
]