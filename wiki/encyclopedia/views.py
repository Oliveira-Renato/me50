from django import http
from django.http import request, HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from django.urls import reverse
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })


def page(request, name):
    content = util.get_entry(name)

    for item in util.list_entries():
        if name.lower() == item.lower():
            name = item
            return render(request, "encyclopedia/page.html", {
            "title":name,
            "content": markdown2.markdown(content)
        })
        elif not util.get_entry(name):
            raise Http404("Page Not Found")

def searchPage(request):
    if request.method == 'POST':
        title = request.POST.get('q')
        
        if title.lower() in [item.lower() for item in util.list_entries()]:
            return HttpResponseRedirect(reverse("page", args=(title,)))
        else:
            results = []
            for item in util.list_entries():
                if title.lower() in item.lower():
                    results.append(item)
            
            return render(request, "encyclopedia/searchPage.html", {
                "entries": results
                })
                    
            

        
        

            
            
                    


   

        



    

    









    #for  item in util.list_entries() :
     #   if name.lower() == item.lower():
     #        return render(request,"encyclopedia/title.html", {
     #       "content": markdown2.markdown(util.get_entry(name)),
    #      "name": name.upper()
    #    })
     #   else:
      #      return Http404('PAGINA NÃO ENCONTRADA!')
    
