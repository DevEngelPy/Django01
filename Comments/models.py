from django.db import models
from Elements.models import Element
# Create your models here.

class Comment(models.Model):

    text = models.TextField()
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    element = models.ForeignKey(Element, related_name="comentario", on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f'comentario: {self.id}'


