from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Palavra(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='palavras')
    palavra = models.CharField(max_length=100)
    dica = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.palavra

    
class Atividade(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=20, choices=[('vitoria', 'Vitória'), ('derrota', 'Derrota')])

    def __str__(self):
        return f"{self.aluno.username} - {self.tema.nome} - {self.resultado}"

