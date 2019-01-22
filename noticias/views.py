from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from noticias.models import Publicacao, Apoiador, Colunista, Categoria


class HomeView(ListView):
    template_name = 'correiocristao/index.html'
    model = Publicacao
