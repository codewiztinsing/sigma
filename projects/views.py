from django.shortcuts import render

from .models import Project, ProjectCategory


def projects(request):
    active_projects = Project.objects.filter(is_active=True)
    featured_project = active_projects.filter(is_featured=True).first()
    grid_projects = active_projects.filter(is_featured=False)
    categories = ProjectCategory.objects.all()

    return render(request, 'projects.html', {
        'active_page': 'projects',
        'featured_project': featured_project,
        'grid_projects': grid_projects,
        'categories': categories,
    })
