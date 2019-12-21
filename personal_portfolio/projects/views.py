from django.shortcuts import render
from .models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def post_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'project_detail.html', {'project':project})

# This is not being used anymore
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
