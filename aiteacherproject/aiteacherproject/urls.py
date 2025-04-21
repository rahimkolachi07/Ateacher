from django.contrib import admin
from django.urls import path
from aiteacherap import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('explainer/', views.explainer, name='explainer'),
    path('ppt-maker/', views.ppt_maker, name='ppt_maker'),
    path('discussion/', views.discussion, name='discussion'),
    path('quiz-builder/', views.quiz_builder, name='quiz_builder'),
    path('lesson-planner/', views.lesson_planner, name='lesson_planner'),

    
]
