# Generated by Django 4.1 on 2024-05-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]