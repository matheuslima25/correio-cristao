from django import forms
from .models import Publicacao
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ('autor', 'titulo', 'texto', 'resumo', 'categoria', 'imagem', 'destaque')


class ContactForm(forms.Form):
    contact_subject = forms.CharField(required=True, label="Assunto: ")
    contact_email = forms.EmailField(required=True, label="E-mail: ")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Mensagem: "
    )

