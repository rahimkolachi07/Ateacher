from django.shortcuts import render
from aiteacherap import *

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def explainer(request):
    return render(request, 'explainer.html')

def ppt_maker(request):
    return render(request, 'ppt_maker.html')

def discussion(request):
    return render(request, 'discussion.html')

def quiz_builder(request):
    return render(request, 'quiz_builder.html')

def lesson_planner(request):
    return render(request, 'lesson_planner.html')

