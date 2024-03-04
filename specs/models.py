from django.db import models


# Create your models here.
class Snippet(models.Model):
    name = models.TextField(max_length=10)
    data = models.TextField(blank=True)
