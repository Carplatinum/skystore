from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category

def home(request):
    products = Product.objects.all() # Получаем все товары из базы данных
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
