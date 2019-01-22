from django.contrib import admin
from .models import Publicacao, Categoria, Colunista, Apoiador

admin.site.register(Publicacao)
admin.site.register(Categoria)
admin.site.register(Colunista)
admin.site.register(Apoiador)
