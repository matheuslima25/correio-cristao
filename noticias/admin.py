from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import Publicacao, Categoria, Colunista, Apoiador, Video, Album, Photo

admin.site.site_title = 'Correio Cristão'
admin.site.site_header = 'Correio Cristão - Painel de Administração'


class PublicacaoAdmin(admin.ModelAdmin):
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/noticias/publicacao/{}/change/">Editar</a>', obj.id)

    def deletar(self, obj):
        return format_html('<a class="btn" href="/admin/noticias/publicacao/{}/delete/">Deletar</a>', obj.id)

    list_display = ('titulo', 'data_criacao', 'destaque', 'editar', 'deletar')
    list_filter = ('data_publicacao',)


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Categoria)
admin.site.register(Colunista)
admin.site.register(Apoiador)
admin.site.register(Video)
admin.site.unregister(Group)
admin.site.register(Album, AlbumAdmin)
