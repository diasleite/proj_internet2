# -*- coding: utf-8 -*-

from django.db import models
from cadastro.models import contato

class contasReceber(models.Model):
    pago = models.BooleanField(verbose_name=u'Pago?',default=False)
    dataMov = models.DateField(verbose_name=u'Data Lancamento')
    dataVencimento = models.DateField(verbose_name=u'Data Vencimento')
    valor = models.DecimalField(decimal_places=2,max_digits=18,verbose_name=u'Valor', default=0)
    descricao = models.CharField(verbose_name=u'Descriçao conta',max_length=40)
    dataPagamento = models.DateField(verbose_name=u'Data Recebimento')
    usuario = models.CharField(verbose_name=u'Usuario',max_length=20)
    contato = models.ForeignKey(contato,blank=True, null=True)

    def __unicode__(self):
      return self.descricao