from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.PositiveIntegerField(verbose_name='Price')
    image = models.ImageField(upload_to='products/', verbose_name='Image')


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'