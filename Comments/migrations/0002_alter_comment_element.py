# Generated by Django 5.0.3 on 2024-04-02 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
        ('Elements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='element',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='Elements.element'),
        ),
    ]
