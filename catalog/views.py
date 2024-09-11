from django.shortcuts import render, redirect
from django.contrib import messages
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')  # Отображение главной страницы


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Обработка данных,
        messages.success(request, 'Ваше сообщение было отправлено успешно!')
        return redirect('home')  # После отправки направляем на главную страницу
    return render(request, 'catalog/contact.html')  # Отображение страницы контактов


def get_product(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/product.html', context)

def get_base(request):
    return render(request, 'catalog/base.html')