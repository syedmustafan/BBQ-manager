# Generated by Django 4.1 on 2022-08-21 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_material_model'),
        ('purchases', '0002_used_material_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='uses', to='inventory.material'),
        ),
    ]
