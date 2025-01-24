from django.shortcuts import render
from store.models import Product, OrderItem

def say_hello(request):
    query_set = Product.objects.defer('description')
    
    return render(request, 'hello.html', {'name': 'Mosh', 'products': query_set})
