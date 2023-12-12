from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name