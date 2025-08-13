from django.core.cache import cache
from .models import Product

def get_products_by_category_cached(category_id):
    """
    Возвращает список опубликованных и доступных продуктов из указанной категории,
    кешируя результат на 5 минут.
    """
    cache_key = f'products_category_{category_id}'
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id, status='published', available=True))
        cache.set(cache_key, products, timeout=60*5)  # кешируем на 5 минут
    return products
