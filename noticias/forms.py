from django import forms
from .models import Publicacao


class PostForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ('autor', 'titulo', 'texto', 'resumo', 'categoria', 'imagem', 'destaque', 'album')


class ContactForm(forms.Form):
    contact_subject = forms.CharField(required=True, label="Assunto: ")
    contact_email = forms.EmailField(required=True, label="E-mail: ")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Mensagem: "
    )
