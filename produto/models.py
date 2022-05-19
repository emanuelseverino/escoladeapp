from django.contrib.auth import get_user_model
from django.db import models


class Produto(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='produtos')
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    codigo_de_barras = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.nome, self.marca)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome', 'marca']
