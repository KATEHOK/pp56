# Generated by Django 4.0.4 on 2022-05-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_user_pet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='title_plural',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Название вида (мн. ч.)'),
        ),
    ]
