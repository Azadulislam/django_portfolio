# Generated by Django 4.0.5 on 2022-07-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='pro_pic_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='pro_pic',
            field=models.FileField(blank=True, upload_to='testimonials/'),
        ),
    ]