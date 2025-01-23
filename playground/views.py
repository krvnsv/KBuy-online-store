from django.shortcuts import render
from django.db.models import Q
from store.models import Product

def say_hello(request):
    # Products: inventory < 10 AND prive < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
