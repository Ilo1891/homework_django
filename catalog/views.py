from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm
from catalog.models import Product, Category, ProductVersion


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/home.html', context)  # Отображение главной страницы


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        print(products)
        return context


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


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
