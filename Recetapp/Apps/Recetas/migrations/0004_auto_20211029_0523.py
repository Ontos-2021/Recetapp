# Generated by Django 3.1.2 on 2021-10-29 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0003_auto_20211029_0519'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecetIngrediente',
            new_name='RecetaIngrediente',
        ),
        migrations.RenameModel(
            old_name='TiendaIngredientes',
            new_name='TiendaIngrediente',
        ),
    ]
