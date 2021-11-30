from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Фото')
    release_date = models.DateField(verbose_name='Релиз', blank=True, null=True)
    lte_exists = models.BooleanField(verbose_name='Наличие LTE', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.name} цена {self.price}"

    def get_slug(self):
        self.slug = slugify(self.name)
