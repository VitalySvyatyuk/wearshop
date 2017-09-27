from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    img = models.CharField(max_length=50)


class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return '%s' % (self.category)
