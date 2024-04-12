from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    #TODO: coloca columnas, basadas en el modelo, para visualizar mejor los datos
    list_display = ('id','text')
    #TODO: agrega una barra de busqueda
    search_fields = ('text','id')
    #TODO: navegacion por fechas
    date_hierarchy = 'date_posted'
    #TODO: ordenamiento
    ordering = ('date_posted',)
    #TODO: filtrado
    list_filter = ('id','date_posted',)
    #TODO: campo editable
    #! es viale en siertos casos
    #list_editable = ('text',)
