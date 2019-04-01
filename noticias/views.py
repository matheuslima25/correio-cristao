from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import views as auth_views

from noticias.forms import PostForm, ContactForm
from noticias.models import Publicacao, Colunista, Video


class HomeView(generic.ListView):
    template_name = 'correiocristao/index.html'
    context_object_name = 'publicacoes_list'

    def get_queryset(self):
        return Publicacao.objects.all().order_by('-data_publicacao')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['colunistas_list'] = Colunista.objects.all()
        context['video_list'] = Video.objects.all().order_by('-data_publicacao')
        context['devocional'] = Publicacao.objects.filter(categoria__slug='devocional').order_by(
            '-data_publicacao')
        context['igrejanahistoria'] = Publicacao.objects.filter(categoria__slug='igrejanahistoria').order_by(
            '-data_publicacao')
        context['mundocristao'] = Publicacao.objects.filter(categoria__slug='mundocristao').order_by(
            '-data_publicacao')
        context['saude'] = Publicacao.objects.filter(categoria__slug='saude').order_by(
            '-data_publicacao')
        context['opiniao'] = Publicacao.objects.filter(categoria__slug='opiniao').order_by(
            '-data_publicacao')
        # Add any other variables to the context here

        return context


class CategoryView(generic.ListView):
    template_name = 'correiocristao/category.html'
    context_object_name = 'publicacoes_list'

    def get_queryset(self):
        return Publicacao.objects.all().order_by('-data_publicacao')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['noticias'] = Publicacao.objects.filter(categoria__slug='noticias').order_by(
            '-data_publicacao')
        context['devocional'] = Publicacao.objects.filter(categoria__slug='devocional').order_by(
            '-data_publicacao')
        context['igrejanahistoria'] = Publicacao.objects.filter(categoria__slug='igrejanahistoria').order_by(
            '-data_publicacao')
        context['entretenimento'] = Publicacao.objects.filter(categoria__slug='entretenimento').order_by(
            '-data_publicacao')
        context['mundocristao'] = Publicacao.objects.filter(categoria__slug='mundocristao').order_by(
            '-data_publicacao')
        context['saude'] = Publicacao.objects.filter(categoria__slug='saude').order_by(
            '-data_publicacao')
        context['opiniao'] = Publicacao.objects.filter(categoria__slug='opiniao').order_by(
            '-data_publicacao')
        # Add any other variables to the context here

        return context

    def category_detail(self, slug):
        category = get_object_or_404(Publicacao, slug=slug)
        return render(self, 'correiocristao/category.html', {'category': category})


class VideoView(generic.ListView):
    template_name = 'correiocristao/video_list.html'
    context_object_name = 'video_list'

    def get_queryset(self):
        return Video.objects.all().order_by('-data_publicacao')

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)

        return context

    def category_detail(self):
        video = get_object_or_404(Video)
        return render(self, 'correiocristao/video_list.html', {'video': video})


class AboutView(TemplateView):
    template_name = 'correiocristao/about.html'


class AdsView(TemplateView):
    template_name = 'correiocristao/advertisement.html'


class PrivacyView(TemplateView):
    template_name = 'correiocristao/privacy.html'


class DoacaoView(TemplateView):
    template_name = 'correiocristao/doacao.html'


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['contact_subject']
            from_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['content']
            try:
                send_mail(subject, message + ' E-mail: ' + from_email, from_email, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "correiocristao/contact.html", {'form': form})


class SuccessView(TemplateView):
    template_name = 'correiocristao/success.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Publicacao
    template_name = 'correiocristao/new_post.html'
    form_class = PostForm
    login_url = '/login/'
    success_url = reverse_lazy('home')


def pesquisar(request):
    termo_busca = request.GET.get('search', None)

    if termo_busca:
        search = Publicacao.objects.filter(texto__icontains=termo_busca)  # case insensitive
    else:
        search = Publicacao.objects.all().order_by('-data_publicacao')

    paginator = Paginator(search, 5)
    page = request.GET.get('page')
    try:
        search = paginator.page(page)
    except PageNotAnInteger:
        search = paginator.page(1)
    except EmptyPage:
        search = paginator.page(paginator.num_pages)
    context = {
        'search': search
    }

    return render(request, 'correiocristao/pesquisa.html', context)


class PostDetailView(DetailView):
    model = Publicacao
    template_name = 'correiocristao/post.html'

    def post_detail(self, slug, pk):
        post = get_object_or_404(Publicacao, slug=slug, pk=pk)
        return render(self, 'correiocristao/post.html', {'post': post})


class VideoDetailView(DetailView):
    model = Video
    template_name = 'correiocristao/video_detail.html'

    def video_detail(self, slug, pk):
        video = get_object_or_404(Video, pk=pk)
        return render(self, 'correiocristao/video_detail.html', {'video': video})


def login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(60 * 60 * 24 * 30)  # one month validity
    return auth_views.LoginView(request, *args, **kwargs)
