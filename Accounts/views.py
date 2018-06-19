# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def index(request):
    return HttpResponse('SpareGear')

