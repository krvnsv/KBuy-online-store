from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    collection.id
    
    collection = Collection.objects.create(title='a', featured_product_id=1)
    collection.id

    return render(request, 'hello.html', {'name': 'Kirill'})
