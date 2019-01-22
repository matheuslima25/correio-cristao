from django.db import models
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
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
    data_publicacao = models.DateTimeField(blank=True, null=True, verbose_name='Data de publicação')
    destaque = models.BooleanField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='')
    imagem = models.ImageField(upload_to='noticias/imagens', null=True, blank=True)

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.titulo


class Apoiador(models.Model):
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
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Colunistas'

    def __str__(self):
        return self.nome

