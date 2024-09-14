from django.urls import path
from catalog.views import home, contact, get_product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('contact/', contact, name='contact'),  # Страница контактов
    path('products/<int:pk>/', get_product, name='product'),
]
