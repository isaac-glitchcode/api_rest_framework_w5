from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Class(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.CharField(max_length=30)
    students_limit = models.IntegerField(validators=[ MaxValueValidator(30)])
   
    init_time = models.TimeField(auto_now=False, auto_now_add=False,)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,)
    
    init_date = models.DateField()
    end_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering=['name']
    
    def __str__(self):
        return self.name
