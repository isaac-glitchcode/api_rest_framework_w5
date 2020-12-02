from django.urls import path
from courses.views import ListCoursesAPIView, UpdateCourseAPIView
urlpatterns = [
    path('', ListCoursesAPIView.as_view(), name='courses' ),
    path('<pk>/',UpdateCourseAPIView.as_view(), name='course'),
    
]
