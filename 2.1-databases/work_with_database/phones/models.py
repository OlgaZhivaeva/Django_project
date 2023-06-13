from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=80, unique=True)