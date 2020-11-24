from django.urls import path
from students.views import get_students, home, get_student

urlpatterns = [
    path('', home ),
    path('students/', get_students ),
    path('student/<id>/', get_student )
]
