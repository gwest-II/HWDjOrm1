from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(null=True)
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(null=True)
