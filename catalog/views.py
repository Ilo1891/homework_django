from django.shortcuts import render, redirect
from django.contrib import messages
from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)  # Отображение главной страницы


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Обработка данных,
        messages.success(request, 'Ваше сообщение было отправлено успешно!')
        return redirect('home')  # После отправки направляем на главную страницу
    return render(request, 'catalog/contact.html')  # Отображение страницы контактов


def get_product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product.html', context)


