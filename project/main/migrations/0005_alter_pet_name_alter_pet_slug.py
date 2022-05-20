# Generated by Django 4.0.4 on 2022-05-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=31, verbose_name='Кличка'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(max_length=31, unique=True, verbose_name='URL'),
        ),
    ]
