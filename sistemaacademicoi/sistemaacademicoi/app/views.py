from django.shortcuts import render
from django.views import View 
from .models import*


class IndexView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'index.html')
  

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupação.html', {'ocupacoes': ocupacoes})

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    
class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituição.html', {'instituicoes': instituicoes})

class AreaView(View):
    def get(self, request, *args, **kwargs):
        areas = Area.objects.all()
        return render(request, 'área.html', {'areas': areas})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all()
        return render(request, 'período.html', {'periodos': periodos})

class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matrícula.html', {'matriculas': matriculas})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliação.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequência.html', {'frequencias': frequencias})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrência.html', {'ocorrencias': ocorrencias})

class Disciplina_cursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_cursos = Disciplina_curso.objects.all()
        return render(request, 'disciplina_curso.html', {'disciplinas_cursos': disciplinas_cursos})

class Tipo_avaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos_avaliacoes = Tipo_avaliacao.objects.all()
        return render(request, 'tipo_avaliação.html', {'tipos_avaliacao': tipos_avaliacoes})