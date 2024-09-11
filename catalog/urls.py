from django.urls import path
from catalog.views import home, contact, get_product

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('contact/', contact, name='contact'),  # Страница контактов
    path('product/<int:pk>', get_product, name='get_product')

]
