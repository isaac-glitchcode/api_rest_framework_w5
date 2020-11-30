from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license = models.CharField(max_length=45)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering=['name']
    
    def __str__(self):
        return self.name