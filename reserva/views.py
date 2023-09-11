from django.shortcuts import render
from reserva.forms import ReservaForms

def inicio(request):
    return render(request, 'index.html')

def reserva(request):
    contexto = {'sucesso': False}
    form = ReservaForms(request.POST or None)

    if form.is_valid():
        contexto['sucesso'] = True
        print(form.cleaned_data['nome'])
        print(form.cleaned_data['telefone'])
        print(form.cleaned_data['dt'])
        print(form.cleaned_data['observacoes'])
    contexto['form'] = form
    return render(request, 'reserva.html', contexto)