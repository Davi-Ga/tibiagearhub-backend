# Generated by Django 4.2 on 2024-06-26 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('level_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('level_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]))])),
                ('class_type', models.CharField(max_length=50)),
            ],
        ),
    ]