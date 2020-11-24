from django.db import models
from classes.models import Class

class Student(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    born_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True) 
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    classes = models.ManyToManyField(Class, related_name="students")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering=['name']
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
