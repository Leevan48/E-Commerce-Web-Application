from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from myapps.cart import Cart
from myapps.forms import CartAddProductForm


def index(request):
    context = {}
    context['products'] = Product.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, 'myapps/index.html', context)


def cart(request):
    context = {}
    return render(request, 'myapps/cart.html', context)


def products(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'myapps/index.html', context)


def categories(request):
    context = {}
    context['categories'] = Category.objects.all()
    return render(request, 'myapps/base.html', context)


def category(request, category):
    context = {}
    context['categories'] = Category.objects.all()
    context['category'] = Category.objects.filter(slug=category).first()
    id = context['category'].id
    context['products'] = Product.objects.filter(category=id)
    return render(request, 'myapps/category.html', context)


def product(request, product):
    context = {}
    context['products'] = Product.objects.all()
    context['product'] = Product.objects.filter(slug=product).first()
    id = context['product'].id
    return render(request, 'myapps/product.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@require_POST
def cart_add(request, product_id):
    crt = Cart(request)
    prod = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        crt.add(product=prod,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    crt = Cart(request)
    prod = get_object_or_404(Product, id=product_id)
    crt.remove(prod)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'myapps/cart.html', {'cart': cart})