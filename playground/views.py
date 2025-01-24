from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    # Products: inventory = price
    product = Product.objects.order_by('unit_price')[0]
    product = Product.objects.latest('unit_price')

    return render(request, 'hello.html', {'name': 'Mosh', 'products': product})
