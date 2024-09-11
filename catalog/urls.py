from django.urls import path
from catalog.views import home, contact, get_product, get_base

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('contact/', contact, name='contact'),  # Страница контактов
    path('products/', get_product, name='products'),
    path('base/', get_base, name='base')

]
