from django.contrib import admin
from Comments.models import Element

@admin.display(description='Title')
def upper_title(obj):
    return f'{obj.id}-{obj.title}'.upper()
