from django.db import models

from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True)
    )
    slug=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    featured = models.BooleanField(default=False)
    slug = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name




