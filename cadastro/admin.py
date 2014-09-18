# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class ContatoAdmin(admin.ModelAdmin):
    pass #mostra todos os campos
 # fields = ['campo1'],['campo2']

admin.site.register(contato,ContatoAdmin)
