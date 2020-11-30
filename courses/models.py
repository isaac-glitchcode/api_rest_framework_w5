from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from professors.models import Professor

class Course(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.CharField(max_length=30)
    
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    
    init_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    
    init_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering=['name']
    
    def __str__(self):
        return self.name
