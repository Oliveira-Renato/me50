from django.shortcuts import render
import markdown2
from . import util

teste = ['CSS','Django','Git','HTML','Python']

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request):
    return render(request,"encyclopedia/title.html", {
        "titles": markdown2.markdown(util.get_entry(teste[0]))
    })

