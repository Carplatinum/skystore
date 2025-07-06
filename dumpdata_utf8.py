import os
import django
from django.core.management import call_command
from io import StringIO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skystore.settings')
django.setup()

if __name__ == "__main__":
    # Дамп данных для catalog.Category
    out_category = StringIO()
    call_command('dumpdata', 'catalog.Category', indent=4, stdout=out_category)
    data_category = out_category.getvalue()

    with open('catalog/fixtures/categories.json', 'w', encoding='utf-8') as f:
        f.write(data_category)

    # Дамп данных для catalog.Product (замените на нужную модель)
    out_product = StringIO()
    call_command('dumpdata', 'catalog.Product', indent=4, stdout=out_product)
    data_product = out_product.getvalue()

    with open('catalog/fixtures/products.json', 'w', encoding='utf-8') as f:
        f.write(data_product)
