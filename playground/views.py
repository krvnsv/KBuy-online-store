from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # None
    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Mosh'})
