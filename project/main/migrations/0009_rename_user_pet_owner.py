# Generated by Django 4.0.4 on 2022-05-21 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_pet_species_alter_pet_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user',
            new_name='owner',
        ),
    ]