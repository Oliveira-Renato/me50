from django.http import request, HttpResponse
from django.shortcuts import render
import markdown2
from . import util


#https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Generic_views

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })


def title(request, name):
    if name not in 'LISTA AQUI':
        return HttpResponse('PAGE NOT FOUND')
    else:
        return render(request,"encyclopedia/title.html", {
        "content": markdown2.markdown(util.get_entry(name)),
        "name": name.upper()
    })

