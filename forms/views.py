from django.shortcuts import render
from forms.forms import PessoaForm

def register_view(request):
    if request.method == "GET":
        form = PessoaForm()
        context = {
            'form': form
        }
        
        return render(request, 'forms/pages/register_view.html', context=context)
    else:
        form - PessoaForm(request.POST)
