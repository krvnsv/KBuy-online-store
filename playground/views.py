from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # keyword=value
    queryset = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
