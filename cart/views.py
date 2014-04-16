from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext

from products.models import Product
from .models import Cart, CartItem
from .forms import ProductQtyForm

def add_to_cart(request):
	try:
		cart_id = request.session['cart_id']
	except Exception:
		cart = Cart()
		cart.save()
		request.session['cart_id'] = cart.id
		cart_id = cart.id

	if request.method == POST:
		form = ProductQtyForm(request.POST)
		if form.is_valid():
			product_slug = form.cleaned_data['slug']
			product_quantity =  form.cleaned_data['quantity']
			try:
				product = Product.object.get(slug=slug)
			except:
				product = None
			new_cart = CartItem(cart=cart_id, product=product, quantity=product_quantity)
			new_cart.save()

			return render_to_response('products/', locals(), context_instance=RequestContext(request))
	
	else:
		raise Http404






