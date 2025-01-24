from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product

def say_hello(request):
    result = Product.objects.filter(collection_id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    
    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
