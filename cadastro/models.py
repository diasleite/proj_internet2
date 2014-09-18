# -*- coding: utf-8 -*-
__author__ = 'mint'

from django.db import models

Status_Lista = (
    ('A','Ativo'),
    ('I','Inativo')

)

class contato(models.Model):
    status = models.CharField(verbose_name=u'Status',max_length=1, default='A', choices=Status_Lista)
    nome = models.CharField(verbose_name=u'Nome',max_length=100)
    doc = models.CharField(verbose_name=u'CPF/CNPJ',max_length=20, unique=True)
    telefone = models.CharField(verbose_name=u'Telefone',max_length=25, null=True,blank=True)#para um campo poder ser opcional null=Treu e blank=True
    logradouro = models.CharField(verbose_name=u'Logradouro',max_length=20)
    endereco = models.CharField(verbose_name=u'Endereço',max_length=40)
    numero = models.PositiveIntegerField(verbose_name=u'Numero')
    bairro = models.CharField(verbose_name=u'Bairro',max_length=20)
    cidade = models.CharField(verbose_name=u'Cidade',max_length=20)
    estado = models.CharField(verbose_name=u'Estado',max_length=20)
    tipoContato = models.CharField(verbose_name=u'Tipo Contato',max_length=20)#tipos: fornecedor ou cliente ou fornecedor/cliente
    dataNascimento = models.DateField(verbose_name=u'Data Nascimento', null=True, blank=True)
    dataCadastro = models.DateField(verbose_name=u'Data Cadastro')
    limiteCompra = models.DecimalField(decimal_places=2,max_digits=18,verbose_name=u'Limite para compra',default=0)
    limiteVenda = models.DecimalField(decimal_places=2,max_digits=18,verbose_name=u'Limite para venda', default=0)
    usuario = models.CharField(verbose_name=u'Usuario',max_length=20, null= True, blank=True)
    email = models.EmailField(verbose_name=u'E-mail',max_length=100)


    def __unicode__(self):
        return self.nome+' / '+self.doc