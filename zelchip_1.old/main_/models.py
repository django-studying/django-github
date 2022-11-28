from django.db import models

# Create your models here.

class Main_barlist(models.Model):
    name = models.CharField(max_length=30)
    urls_field = models.URLField(max_length=200, default='http://')
    
    def __str__(self):
        return self.name
