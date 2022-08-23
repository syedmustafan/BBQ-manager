# Generated by Django 4.1 on 2022-08-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_material_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.CharField(choices=[('GR', 'Gramms'), ('PC', 'Pieces')], max_length=3, verbose_name='material_measurment_units'),
        ),
    ]
