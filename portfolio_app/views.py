from django.shortcuts import render
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio_app/portfolio.html', context)