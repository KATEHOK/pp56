# Generated by Django 4.0.4 on 2022-05-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_pet_options_pet_slug_alter_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(max_length=15, unique=True, verbose_name='URL'),
        ),
    ]