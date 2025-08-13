from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Product, Category
from .forms import ProductForm
from .services import get_products_by_category_cached  # Импорт сервисной функции


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


@method_decorator(cache_page(60 * 15), name='dispatch')  # Кешируем страницу детального просмотра продукта на 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 'draft'
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner != user:
            raise Http404('У вас нет прав на редактирование этого продукта')
        return product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner == user or user.groups.filter(name='Модератор продуктов').exists():
            return product
        raise Http404('У вас нет прав на удаление этого продукта')


class ProductsByCategoryView(ListView):
    model = Product
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_by_category_cached(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = Category.objects.get(pk=category_id)
        return context
