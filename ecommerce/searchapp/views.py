from django.shortcuts import render
from django.db.models import Q
from ecartapp.models import Products

# Create your views here.

def SearchResult(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Products.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'product':product})