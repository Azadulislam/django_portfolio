from pathlib import Path
from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models


def file_name(path):
    def f(instance, filename):
        ext = Path(filename).suffix
        return path+filename
    return f

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
    profile_pic = models.ImageField(upload_to=file_name("profile_pic/"), blank=False) # Install pillow( pip install pillow)
    facebook = models.CharField(max_length=255, blank=False)
    linkedin = models.CharField(max_length=255, blank=False)
    skype = models.CharField(max_length=255, blank=False)
    twitter = models.CharField(max_length=255, blank=False)
    resume_url = models.FileField(upload_to="resume/", blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


