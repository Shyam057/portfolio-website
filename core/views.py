from django.shortcuts import render
from .models import About, Skill, Education, Experience
from portfolio_app.models import Project

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)

    context = {
        'about': about,
        'skills': skills,
        'education': education,
        'experience': experience,
        'featured_projects': featured_projects,
    }
    return render(request, 'core/home.html', context)

def about(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()

    context = {
        'about': about,
        'skills': skills,
        'education': education,
        'experience': experience,
    }
    return render(request, 'core/about.html', context)