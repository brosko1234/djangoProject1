from django.db import models


class Basic(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=80)
    description = models.TextField(default=0)
    image_small = models.ImageField(upload_to="trade/")
    image_big = models.ImageField(upload_to="trade/")

    def __str__(self):
        return self.title
