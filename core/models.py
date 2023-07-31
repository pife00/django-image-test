from django.db import models

# Create your models here.

class imageData(models.Model):
    image = models.ImageField(upload_to="core_images",blank=True,null=True)
