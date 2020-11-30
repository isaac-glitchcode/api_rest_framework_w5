from django.urls import path
from courses.views import courses, course
urlpatterns = [
    path('courses/', courses),
    path('course/<course_id>/', course),
    
]
