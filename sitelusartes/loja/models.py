from django.db import models

# Create your models here.

class Empresa (models.Model):
    nome_empresa = models.CharField(max_length = 100)
    logo_empresa = models.CharField(max_length = 30)

    def __str__ (self):
        return self.nome_empresa

class Categoria (models.Model):
    nome_categoria = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nome_categoria


class Produto (models.Model):
    nome_produto = models.CharField(max_length=100)
    descricao_produto = models.CharField(max_length=200)
    valor_produto = models.FloatField(default=0)
    quantidade_produto = models.IntegerField(default=0)
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    def __str__ (self):
        return self.nome_produto
