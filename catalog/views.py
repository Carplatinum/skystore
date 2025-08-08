from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin   # импорт миксина ограничения доступа
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)
from .models import Product
from .forms import ProductForm

# Главная страница (тот же продуктовый список, как HomeView)
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

# Страница контактов
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# Детальная страница продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# ========== CRUD для продуктов ==========
# Список продуктов — публичный, доступ без авторизации
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

# Создание продукта — доступ только для авторизованных пользователей
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

# Редактирование продукта — доступ только для авторизованных пользователей
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

# Удаление продукта — доступ только для авторизованных пользователей
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
