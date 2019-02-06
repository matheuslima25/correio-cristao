from django.db import models
from django.urls import reverse
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Publicacao(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=50, default='')
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    destaque = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default='')
    imagem = models.ImageField(upload_to='noticias/imagens', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo


class Apoiador(models.Model):
    ordem = models.CharField(max_length=2, blank=True, null=True)
    imagem = models.ImageField()
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Apoiadores'

    def __str__(self):
        return self.nome


class Colunista(models.Model):
    foto = models.ImageField(upload_to='colunistas/fotos', null=True, blank=True)
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Colunistas'

    def __str__(self):
        return self.nome


class Video(models.Model):
    nome = models.CharField(max_length=50, default='')
    link = models.URLField()
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default='')

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.nome
