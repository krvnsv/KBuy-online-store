from django.shortcuts import render
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Order, OrderItem, Product, Collection
from tags.models import TaggedItem

def say_hello(request):
    query_set = Product.objects.raw('SELECT id, title FROM store_product')

    return render(request, 'hello.html', {'name': 'Kirill', 'result': list(query_set)})
