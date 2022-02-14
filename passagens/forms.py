from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.CharField(label='Ida', widget=DatePicker())
    volta = forms.CharField(label='Volta', widget=DatePicker())
    pesquisa = forms.CharField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe = forms.ChoiceField(label="Classe do vôo", choices=tipos_de_classe,)
    informacoes = forms.CharField(
        label="Informações extras.",
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label="E-mail")