# Generated by Django 3.1.2 on 2021-10-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='tiempo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='vegano',
            field=models.BooleanField(null=True),
        ),
    ]