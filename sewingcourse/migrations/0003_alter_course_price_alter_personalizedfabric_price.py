# Generated by Django 4.0.6 on 2022-07-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewingcourse', '0002_personalizedfabric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='personalizedfabric',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
