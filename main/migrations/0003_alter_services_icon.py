# Generated by Django 4.0.5 on 2022-07-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.FileField(upload_to='services/'),
        ),
    ]