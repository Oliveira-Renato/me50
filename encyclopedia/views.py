from django import http
from django.http import request, HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from django.urls import reverse
import markdown2
from . import util
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })


def page(request, name):
    content = util.get_entry(name)

    #return the page to edit the actual content
    if request.method == 'POST':
        return render(request, 'encyclopedia/edit.html', {
            'title':name,
            'content':content
        })

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
    else:#return a random page
        rand_page = random.choice(util.list_entries())
        return HttpResponseRedirect(reverse("page", args=(rand_page,)))


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title.lower() not in [x.lower() for x in util.list_entries()]:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("page", args=(title,)))
        else:
            html = '<html><body><h1 style="color: #b22222;">Page "%s" already exist!</h1></body></html>' % title
            return HttpResponse(html)
            
    else:
        return render(request, "encyclopedia/create.html")



def edit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("page", args=(title,)))



 