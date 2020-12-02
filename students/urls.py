from django.urls import path
from students.views import ListStudentsAPIView, UpdateStudentAPIView

urlpatterns = [
    path('', ListStudentsAPIView.as_view(), name='students'),
    path('<pk>/', UpdateStudentAPIView.as_view(), name='student'),
]