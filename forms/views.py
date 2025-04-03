from django.shortcuts import render, redirect
from forms.forms import PessoaForm
 
def register_view(request):
    form = PessoaForm()
    context = {
        'form': form
    }
    return render(request, 'forms/pages/register_view.html', context=context)
    