from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # отображение в списке
    search_fields = ('name',)      # поиск по name (можно добавить и description, если нужно)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # поля для отображения в списке
    list_filter = ('category',)                         # фильтрация по категории
    search_fields = ('name', 'description')             # поиск по name и description
