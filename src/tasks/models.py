from django.db import models
import datetime

# Create your models here.

class Task(models.Model):
    pid = models.IntegerField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    person = models.CharField(max_length=120, default = "None")
    date = models.DateField(default=datetime.date.today)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
