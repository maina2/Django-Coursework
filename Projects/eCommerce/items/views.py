from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()[:20]  # Get the first 20 items
    return render(request, 'product_list.html', {'products': products})
