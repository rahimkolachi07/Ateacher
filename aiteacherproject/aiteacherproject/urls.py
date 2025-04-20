from django.contrib import admin
from django.urls import path
from aiteacherap import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explainer/', views.explainer, name='explainer'),
    path('dashboard/ppt-maker/', views.ppt_maker, name='ppt_maker'),
    path('dashboard/discussion/', views.discussion, name='discussion'),
    path('dashboard/quiz-builder/', views.quiz_builder, name='quiz_builder'),
    path('dashboard/lesson-planner/', views.lesson_planner, name='lesson_planner'),

    
]
