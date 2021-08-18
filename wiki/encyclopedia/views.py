from django.shortcuts import render
import markdown2
from . import util

teste = ['CSS','Django','Git','HTML','Python']

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request):
    #TRY TO USE THIS FUNCTION
    #def pegaNome(nome): <---nome do titulo da pesquisa 
    #   for i in listNome:
    #       if i == nome:
    #           util.get_entry(nome)
    #       else:
    #           return Null
    return render(request,"encyclopedia/title.html", {
        "titles": markdown2.markdown(util.get_entry(teste[0]))
    })

