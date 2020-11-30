from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="students")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering=['name']
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
