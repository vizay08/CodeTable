from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Code(models.Model):
    code = models.CharField(max_length=6)
    token = models.TextField()
    language = models.CharField(max_length=12,default="JAVA")
    is_running = models.BooleanField(default=False)
    is_writable = models.BooleanField(default=False)
    shared_code = models.CharField(max_length=6)
    
