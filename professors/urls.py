from django.urls import path
from professors.views import professors, professor

urlpatterns = [
    path('professors/', professors),
    path('professor/<professor_id>/', professor)
]