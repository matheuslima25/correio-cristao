from django.db import models
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Colunista(models.Model):
    foto = CloudinaryField('imagem', null=True, blank=True)
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100, null=True, blank=True, default='')
    facebook = models.CharField(max_length=500, null=True, blank=True, default='')
    instagram = models.CharField(max_length=500, null=True, blank=True, default='')
    telefone = models.CharField(max_length=20, null=True, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Colunistas'

    def __str__(self):
        return self.nome


class Album(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField("Título (opcional)", max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Albuns'

    def __str__(self):
        return self.titulo


class Photo(models.Model):
    image = CloudinaryField('Imagem')
    album = models.ForeignKey(Album, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.pk, public_id)


class Publicacao(models.Model):
    autor = models.ForeignKey(Colunista, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=500, default='')
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    destaque = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default='')
    imagem = CloudinaryField('Imagem', null=True, blank=True)
    album = models.ForeignKey('Album', blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    @property
    def autor_name(self):
        return self.autor.nome

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo


class Apoiador(models.Model):
    ordem = models.CharField(max_length=2, blank=True, null=True)
    imagem = CloudinaryField('imagem')
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Apoiadores'

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
