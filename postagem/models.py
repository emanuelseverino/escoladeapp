from django.contrib.auth import get_user_model
from django.db import models


class Postagem(models.Model):
    foto = models.ImageField(upload_to='postagem', blank=True, null=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=200)
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s %s' % (self.titulo, self.autor.nome, self.autor.sobrenome)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ('-criado',)
