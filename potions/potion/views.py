"""
views.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Provide view responses for the chirper app.

"""

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Potion


# Create your views here.
def home(request):
    template_name = "potion/brewery.html"
    potion_list = Potion.objects.all()
    context = {
        "potion_list": potion_list,
    }

    return render(request, template_name, context)
