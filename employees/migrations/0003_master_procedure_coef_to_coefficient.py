# Generated by Django 4.1 on 2022-08-22 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_coef_to_coefficient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterprocedure',
            old_name='coeffitient',
            new_name='coefficient',
        ),
    ]
