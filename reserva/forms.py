from django import forms

class ReservaForms(forms.Form):
    nome = forms.CharField(max_length=50, label="Nome do Pet")
    telefone = forms.CharField(max_length=11, label="Telefone")
    dt = forms.DateField(label="Dia da Reserva")
    observacoes = forms.CharField(widget=forms.Textarea, label="Observações")    