from django.db import models
from  django.core.exceptions import ValidationError
# Create your models here
class Category(models.Model):

    title = models.CharField(max_length = 255)
    slug = models.CharField( max_length=50)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.title

class Type(models.Model):

    title = models.CharField(max_length = 255)
    slug = models.CharField( max_length=50)
    class Meta:
        verbose_name = ("Type")
        verbose_name_plural = ("Types")

    def __str__(self):
        return self.title

class Element(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 255, blank = True)
    description = models.TextField()
    price = models.DecimalField( max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name = ("Categorias"), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, verbose_name=("Tipos"), on_delete=models.CASCADE)
    
    #TODO: validacion ejemplo
    
    def clear(self):
        if self.price < 0:
            raise ValidationError('el precio debe se mayor a 0')
    class Meta:
        verbose_name = ("Element")
        verbose_name_plural = ("Elements")

    def __str__(self):
        return self.title
