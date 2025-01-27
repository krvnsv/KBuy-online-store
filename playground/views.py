from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

def say_hello(request):
    collection = Collection(pk=11)
    # collection.delete()

    Collection.objects.filter(id__gt=10).delete()

    return render(request, 'hello.html', {'name': 'Kirill'})
