from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    query_set = Product.objects.all()
    query_set[0]
    list(query_set)
    
    return render(request, 'hello.html', {'name': 'Mosh'})
