from typing import Any
from django.contrib import admin
from .models import Type, Element, Category
from django.utils.text import slugify


# Register your models here.
#TODO: esto se coloca asi debido  a que tienen campos similares
@admin.register(Category, Type)
class CategotyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    #list_display = ['upper_title',]
    list_display = ('id','title','category','type')
    #TODO: con esas tupas se puede reacomodar mejor el formulario
    fields = (('title','slug'),'description','price',('category','type'))
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not(change) and obj.slug == '':
            obj.slug = slugify(obj.title)
        if obj.slug == '':
            obj.slug = slugify(obj.title)
        return super().save_model(request, obj, form, change)