from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    
    def __str__(self):
        return f'{self.nome}, {self.uf}'

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Ocupação"

    def __str__(self):
        return f'{self.nome}'

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    datanasci = models.DateField()
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Pessoa"

    def __str__(self):
        return f'{self.nome},{self.pai},{self.mae},{self.cpf},{self.datanasci},{self.email},{self.cidade},{self.ocupacao}'

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Instituição"
             
    def __str__(self):
        return f'{self.nome}, {self.site}, {self.telefone}, {self.cidade}'

class Area(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Área"
             
    def __str__(self):
        return f'{self.nome}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.CharField(max_length=100)
    duracao_meses = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Curso"
             
    def __str__(self):
        return f'{self.nome},{self.carga_horaria_total},{self.duracao_meses},{self.area},{self.instituicao}'

class Periodo(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Período"
             
    def __str__(self):
        return f'{self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Disciplina"
             
    def __str__(self):
        return f'{self.nome},{self.area}'

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    
    class Meta:
        verbose_name_plural = "Matrícula"
             
    def __str__(self):
        return f'{self.instituicao}, {self.curso}, {self.pessoa},{self.data_inicio},{self.data_termino}'
    
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Avaliação"
             
    def __str__(self):
        return f'{self.descricao},{self.curso}, {self.disciplina}'

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Frequência"
             
    def __str__(self):
        return f'{self.curso} , {self.disciplina} , {self.pessoa}, {self.numero_faltas}'

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Turma"
             
    def __str__(self):
        return f'{self.nome} , {self.turno}'

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Ocorrência"
             
    def __str__(self):
        return f'{self.descricao} , {self.data} , {self.curso} - {self.disciplina}, {self.pessoa}'

class Disciplina_curso(models.Model):
    disciplina = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Disciplina_Cursos"
             
    def __str__(self):
        return f'{self.disciplina}, {self.carga_horaria},{self.curso} {self.periodo}'

class Tipo_avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Tipo_avaliação"
             
    def __str__(self):
        return f'{self.nome} '

      
