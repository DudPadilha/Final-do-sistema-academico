"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('área/', AreaView.as_view(), name='área'),
    path('avaliação/', AvaliacaoView.as_view(), name='avaliação'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('disciplina_curso/', Disciplina_cursoView.as_view(), name='disciplina_curso'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('frequência/', FrequenciaView.as_view(), name='frequência'),
    path('instituição/', InstituicaoView.as_view(), name='instituição'),
    path('matrícula/', MatriculaView.as_view(), name='matrícula'),
    path('ocorrência/', OcorrenciaView.as_view(), name='ocorrência'),
    path('ocupação/', OcupacaoView.as_view(), name='ocupação'),
    path('período/', PeriodoView.as_view(), name='período'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('tipo_avaliação/', Tipo_avaliacaoView.as_view(), name='tipo_avaliação'),
    path('turma/', TurmaView.as_view(), name='turma'),

]
