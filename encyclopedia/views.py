
import markdown2

from django import forms
from django.shortcuts import render
from . import util

class SearchForm(forms.Form):
    search_query =  forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_query": SearchForm()
    })

def title(request, entry_name):
    return render(request, "encyclopedia/entry.html", 
    {
        "entry": markdown2.markdown(util.get_entry(entry_name))
    })
