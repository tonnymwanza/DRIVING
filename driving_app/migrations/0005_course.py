# Generated by Django 4.1 on 2024-05-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_app', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
            ],
        ),
    ]