# Generated by Django 4.1 on 2022-08-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='material_name')),
                ('unit', models.CharField(choices=[('GR', 'Gramms'), ('PC', 'Pieces')], max_length=2, verbose_name='material_measurment_units')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='material_price')),
                ('archived', models.BooleanField(default=False, verbose_name='is_archived')),
            ],
            options={
                'db_table': 'materials',
            },
        ),
    ]
