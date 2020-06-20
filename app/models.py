from django.db import models
#Django Object Relational Mapper
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.TextField(null=True, verbose_name='descrição')
    is_active = models.BooleanField(default=True, verbose_name='ativo?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    is_active = models.BooleanField(default=True, verbose_name='ativo?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'produto'