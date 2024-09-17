from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/home.html', context)  # Отображение главной страницы


class ProductListView(ListView):
    model = Product


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         # Обработка данных,
#         messages.success(request, 'Ваше сообщение было отправлено успешно!')
#         return redirect('home')  # После отправки направляем на главную страницу
#     return render(request, 'catalog/contact.html')  # Отображение страницы контактов


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"
    extra_context = {"title": "Контакты"}


# def get_product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#     }
#     return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    model = Product


