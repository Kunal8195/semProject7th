from django.shortcuts import render
from .models import cart_items
from django.http import HttpResponse

# Create your views here.
def add_to_cart(request):
	if request.method == 'POST':
		product_id = request.POST['product_id']
		productname = request.POST['productname']
		image = request.POST['image']
		price = request.POST['price']
		
	cart_items.objects.create(
	    product =  product_id,
		productname = productname,
		image = image,
		price = price
	)
	
	return HttpResponse('')

def delete_from_cart(request):
	if request.method == 'POST':
		cart_id = request.POST['cart_id']

	cart_items.objects.filter(pk=cart_id).delete();

	return HttpResponse('')