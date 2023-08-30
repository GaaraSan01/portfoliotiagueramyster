from django.shortcuts import render
from portifolio.models import Projects, ImageFieldsProject


def index(request):
    return render(request, 'index.html')

def projetos(request):
    context = {'current_page': 'projetos'}
    projects = Projects.objects.order_by("date_publicated").filter(public_project=True)
    context['cards'] = projects
    return render(request, 'portifolio.html', context)

def projeto(request, project_id):
    project = Projects.objects.get(pk=project_id)
    project_images = project.images.all() 
    return render(request, 'project.html', {'project': project, 'children': project_images})

def sobre(request):
    context = {'current_page': 'sobre'}
    return render(request, 'sobre.html', context)

def filtro(request, category):
    context = {
        'filtro_um': 'projetos/SITES',
        'filtro_dois': 'projetos/MOBILE',
        'filtro_tres': 'projetos/LANDIN_PAGE'
    }
    projects = Projects.objects.order_by('date_publicated').filter(public_project=True, category=category)
    context['cards'] = projects

    return render(request, 'portifolio.html', context)