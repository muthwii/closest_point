from django.db import models


# Create your models here.
class closest_point(models.Model):  
  
    points = models.CharField(max_length=100) 
    closest_points_pair = models.CharField(max_length=100)      
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
 
    
