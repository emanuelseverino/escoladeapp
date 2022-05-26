from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    visto = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ('modificado',)

