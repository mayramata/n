# Generated by Django 4.0.6 on 2022-07-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costureras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_costurera', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date_register', models.DateTimeField()),
                ('home', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='name_empleado',
        ),
    ]
