# Generated by Django 4.1 on 2024-05-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0010_alter_application_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='driving_app.course'),
        ),
    ]
