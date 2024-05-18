# Generated by Django 4.1 on 2024-05-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0003_rename_user_appointment_appointee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]