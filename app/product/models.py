import uuid

from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField('Code', max_length=20)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', blank=True)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    code = models.CharField('Code', max_length=36, blank=True)
    reference = models.CharField('Reference', max_length=20)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description', blank=True)
    tecnical_descripcion = models.TextField('Tecnical Desc', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    score = models.DecimalField('Score', max_digits=3, decimal_places=2,
                                default=0.00)
    provider = models.CharField('Provider', max_length=36)
    active = models.BooleanField('Active', default=True)

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.id:
            self.code = uuid.uuid4()
        super(Product, self).save(*args, **kwargs)


class MediaResource(models.Model):
    label = models.CharField('Label', max_length=30)
    path = models.ImageField('Path', upload_to='resources/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='resources')

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'product_media_resource'
        verbose_name_plural = 'MediaResources'
