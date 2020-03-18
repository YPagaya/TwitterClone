from django.db import models
from django.utils import timezone 


class post(models.Model):
    post_text = models.CharField(max_length=140)
    post_date = models.DateTimeField('date posted')
    
    def __str__(self):
        return self.post_text