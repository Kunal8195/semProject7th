from django.shortcuts import render,render_to_response
from .models import product, category
from django.core.context_processors import csrf
from cart.models import cart_items

# Create your views here.

def products(request):
    c={}
    c.update(csrf(request))
    c['full_name']=request.user.username
    c['pro']=product.objects.all()
    c['catg']=category.objects.all()
    return render_to_response('products/product.html',c)

def product_info(request, product_id):
    c={}
    c.update(csrf(request))
    c['p_t'] = product.objects.get(pk=product_id)
    c['full_name'] = request.user.username
    return render_to_response('products/product-details.html',c)

def cart(request):
    c={}
    c.update(csrf(request))
    c['cart1'] = cart_items.objects.all()
    c['full_name'] = request.user.username
    return render_to_response('products/cart.html',c)

def checkout(request):
    return render_to_response('products/checkout.html',{'full_name':request.user.username})





