# Generated by Django 4.1 on 2024-05-19 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0011_alter_application_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='course',
        ),
    ]