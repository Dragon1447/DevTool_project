from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    detail = models.TextField()

    def __str__(self):
        return self.name
