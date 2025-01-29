from django.shortcuts import render

def say_hello(request):
    
    return render(request, 'hello.html', {'name': 'Kirill', 'result': list(query_set)})
