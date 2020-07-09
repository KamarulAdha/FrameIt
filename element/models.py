from django.db import models

# Create your models here.
class Element(models.Model):
    element_name = models.CharField(max_length=255, unique=True)
    element_tag = models.CharField(max_length=255)
    element_type = models.CharField(max_length=255)
    element_img = models.ImageField(upload_to='elements/')
    creator_tag = models.CharField(max_length=255)
    creator_link = models.CharField(max_length=255)

    def __str__(self):
        return self.element_name
