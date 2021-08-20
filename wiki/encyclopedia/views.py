from django.http import request, HttpResponse, Http404
from django.shortcuts import render

import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })


def title(request, name):
    content = util.get_entry(name)

    for item in util.list_entries():
        if name.lower() == item.lower():
            name = item
            return render(request, "encyclopedia/title.html", {
            "title":name,
            "content": markdown2.markdown(content)
        })
        elif not util.get_entry(name):
            raise Http404("Page does not exist")

    

    









    #for  item in util.list_entries() :
     #   if name.lower() == item.lower():
     #        return render(request,"encyclopedia/title.html", {
     #       "content": markdown2.markdown(util.get_entry(name)),
    #      "name": name.upper()
    #    })
     #   else:
      #      return Http404('PAGINA NÃO ENCONTRADA!')
    
