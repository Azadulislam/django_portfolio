from django.http import HttpResponse
from django.shortcuts import render

from .models import Administrator, Skill


def index(request):
    try:
        administrator = Administrator.objects.all()[0]
        skills = Skill.objects.all()
    except IndexError:
        return HttpResponse('Create Object for administrator')
    return render(request, 'index.html', {"admin":administrator, "skills":skills})
