from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),  # Главная страница
    path(
        "contact/", ContactTemplateView.as_view(), name="contacts"
    ),  # Страница контактов
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
]
