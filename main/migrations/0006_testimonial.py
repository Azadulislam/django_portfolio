# Generated by Django 4.0.5 on 2022-07-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('comment', models.TextField()),
                ('pro_pic', models.FileField(upload_to='testimonials/')),
            ],
        ),
    ]