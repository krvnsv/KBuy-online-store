from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, Customer

def say_hello(request):
    query_set = Customer.objects.annotate(new_id=F('id') + 1)
    
    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(query_set)})
