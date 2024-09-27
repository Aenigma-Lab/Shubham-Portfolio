# models.py
# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return self.name
