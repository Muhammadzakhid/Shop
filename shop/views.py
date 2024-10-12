
from django.shortcuts import render
from urllib import request
from django.views.generic import ListView, DetailView
from .models import Product

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.views.generic import CreateView

from django.db.models  import Q


def search_views(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.none()


    context = {
        'products': products,
        'query' : query,
    }
    
    return render(request, 'main/search_results.html', context)

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('product_list')

class SignInView(LoginView):
    form_class = SignInForm
    template_name = "registration/sign_in.html"
    
    
    def get_success_url(self):
        return reverse_lazy('product_list')


def logout_view(request):
    logout(request)
    return redirect('product_list')


def custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)