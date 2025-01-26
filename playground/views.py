from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Customer

def say_hello(request):
    query_set = Customer.objects.annotate(orders_count=Count('order'))

    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(query_set)})
