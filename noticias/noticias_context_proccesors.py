from .models import Publicacao, Categoria, Apoiador


def featured_posts(request):
    posts = Publicacao.objects.filter(destaque=True).order_by('-data_publicacao')
    return {'featured_posts': posts}


def apoiadores(request):
    apoiador = Apoiador.objects.all()
    return {'apoiadores': apoiador}


def categories(request):
    category = Categoria.objects.all()
    return {'categories': category}
