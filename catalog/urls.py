from django.urls import path
from .views import (
    HomeView,
    ContactsView,
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView,
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('products/', ProductListView.as_view(), name='product_list'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Путь для отображения продуктов по категории
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
