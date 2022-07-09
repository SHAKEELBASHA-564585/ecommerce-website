from django.http import Http404
from django.shortcuts import render
from .models import Item


# Create your views here.

def home_page(req):
    items = Item.objects.all()
    return render(req,"shakeel_app/index.html",{"items": items})


def get_item(req,pk):
    try:
        item = Item.objects.get(pk=pk)
        return render(req,"shakeel_app/item_home.html",{"item": item})
    except:
        raise Http404("Item Doesn't exists")