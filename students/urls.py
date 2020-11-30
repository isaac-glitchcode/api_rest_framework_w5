from django.urls import path
# from students.views import home,StudentView, StudentFormView, get_student
from students.views import students, student
app_name='students'
urlpatterns = [
    path('students/', students),
    path('student/<student_id>/', student),
    # path('', home, name='home' ),
    # path('student', StudentView.as_view(), name='list' ),
    # path('add_student', StudentFormView.as_view(), name='add_student' ),
    # path('student/<id>/', get_student, name='detail' )
]