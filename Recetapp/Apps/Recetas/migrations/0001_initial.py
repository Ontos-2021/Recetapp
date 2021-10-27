# Generated by Django 3.1.2 on 2021-10-27 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('horario', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('abreviacion', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ingrediente', models.ManyToManyField(to='Recetas.Ingrediente')),
            ],
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='tienda',
            field=models.ManyToManyField(to='Recetas.Tienda'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Recetas.unidad'),
        ),
    ]