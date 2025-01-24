from django.shortcuts import render
from store.models import Product, Order

def say_hello(request):
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(query_set)})
