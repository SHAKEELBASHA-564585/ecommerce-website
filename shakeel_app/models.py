from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.TextField()
    image_url = models.TextField()
    original_price = models.IntegerField()
    current_price = models.IntegerField()
    item_description = models.TextField()