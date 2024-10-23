from django.db import models

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True)
    image = models.ImageField(default='', blank=True)
    
    def __str__(self):
        return self.title