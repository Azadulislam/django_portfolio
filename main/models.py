import datetime
from email.mime import image
from operator import mod
from pathlib import Path
from uuid import uuid4

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models


class Administrator(models.Model):
    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)
    title = models.CharField(max_length=255, blank=False)
    short_desc = models.TextField(blank=False)
    long_desc = RichTextField()
    position = models.CharField(max_length=55, blank=False)
    email = models.EmailField(max_length=55, blank=False)
    contact_no = models.CharField(max_length=55, blank=False)
    address = models.CharField(max_length=255, blank=False)
    profile_pic = models.ImageField(upload_to="profile_pic/", blank=False) # Install pillow( pip install pillow)
    facebook = models.CharField(max_length=255, blank=False)
    linkedin = models.CharField(max_length=255, blank=False)
    skype = models.CharField(max_length=255, blank=False)
    twitter = models.CharField(max_length=255, blank=False)
    resume = models.FileField(upload_to="resume/", blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Skill(models.Model):
    title = models.CharField(max_length=55, blank=False, unique=True)
    percentage = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

class Services(models.Model):
    icon = models.FileField(upload_to="services/", blank=False)
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title


class Summery(models.Model):
    customer = models.IntegerField(blank=True)
    project_completed = models.IntegerField(blank=True)
    reveiw = models.IntegerField(blank=True)
    running_project = models.IntegerField(blank=True)

    def __str__(self):
        return "Addministrator Summery"


class Portfolio(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    image = models.FileField(upload_to='portfolio/', blank=False)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=55, blank=False)
    comment = models.TextField(blank=False)
    pro_pic = models.FileField(upload_to='testimonials/', blank=True)
    pro_pic_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class SiteSetting(models.Model):
    title = models.CharField(max_length=255, blank=False)
    primary_color = ColorField(format='hexa',blank=False)
    copy_right = models.CharField(max_length=255, blank=False)
    banner_bg = models.FileField(upload_to='site/', blank=False)
    skill_bg = models.FileField(upload_to='site/', blank=False)
    summery_bg = models.FileField(upload_to='site/', blank=False)
    testimonial_bg = models.FileField(upload_to='site/', blank=False)
    contact_bg = models.FileField(upload_to='site/', blank=False)
    site_logo = models.FileField(upload_to='site/', blank=False)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True)

    def __str__(self):
        return self.title

class WonerTitle(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name
