# Generated by Django 4.0.6 on 2022-07-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_materials', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]