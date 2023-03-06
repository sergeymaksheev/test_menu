
from django.views import generic
from django.shortcuts import render

from menu.models import MenuItem


def index(request, pk=None):
    menu = MenuItem.objects.all()
    context = {
        'menu': menu,
        'title': 'Меню'
    }
    return render(request, 'menu/index.html', context=context)
