from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(Area)
admin.site.register(Curso)
admin.site.register(Periodo)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Ocorrencia)
admin.site.register(Disciplina_curso)
admin.site.register(Tipo_avaliacao)