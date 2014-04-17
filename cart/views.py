from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, Http404

from products.models import Product
from .models import Cart, CartItem
from .forms import ProductQtyForm

def add_to_cart(request):
	request.session.set_expiry(3000)
	try:
		cart_id = request.session['cart_id']
	except Exception:
		cart = Cart()
		cart.save()
		request.session['cart_id'] = cart.id
		cart_id = cart.id

	if request.method == 'POST':
		form = ProductQtyForm(request.POST)
		if form.is_valid():
			product_slug = form.cleaned_data['slug']
			product_quantity =  form.cleaned_data['quantity']

			try:
				product = Product.objects.get(slug=product_slug)
			except:
				product = None

			try:
				cart = Cart.objects.get(id=cart_id)
			except:
				cart = None

			new_cart, created = Cart.objects.get_or_create(cart=cart, product=product)
			new_cart.quantity = product_quantity
			new_cart.save()

			if created:
				print "Created!"

			return HttpResponseRedirect('/products/')
		return HttpResponseRedirect('/contact/')
	
	else:
		raise Http404


def view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = False

	if cart == False or cart.active == False:
		message = 'Your cart is empty'

	if cart and cart.active:
		cart = cart

	return render_to_response('cart/view.html', locals(), context_instance=RequestContext(request))



