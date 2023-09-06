from django.urls import path
from portifolio.views import index, projetos, projeto, sobre, filtro

urlpatterns = [
    path('', index, name='index'),
    path('projetos/', projetos, name='projetos'),
    path('projeto/<int:project_id>/', projeto, name='projeto'),
    path('sobre', sobre, name='sobre'),
    path('projetos/<str:category>', filtro, name='filtro')
]