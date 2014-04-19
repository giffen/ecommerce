from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, Http404

from products.models import Product
from .models import Cart, CartItem
from .forms import ProductQtyForm

import stripe
stripe.api_key = 'sk_test_0hjKwnrysWtUmhFd8lAEtQEE'

def add_to_cart(request):
	request.session.set_expiry(0)
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

			new_cart, created = CartItem.objects.get_or_create(cart=cart, product=product)
			#print product_quantity, new_cart.quantity
			'''
			if new_cart.quantity > 0:
				new_cart.quantity = product_quantity
				new_cart.total = int(new_cart.quantity) * new_cart.product.price
				new_cart.save()
			else:
				pass
			'''
			new_cart.quantity = product_quantity
			new_cart.total = int(new_cart.quantity) * new_cart.product.price
			new_cart.save()
			
			if created:
				print "Created!"

			return HttpResponseRedirect('/cart/')
		return HttpResponseRedirect('/contact/')
	
	else:
		raise Http404


def view(request):
	# request.session.set_expiry(30)
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = False

	if cart == False or cart.active == False:
		message = 'Your cart is empty'

	if cart and cart.active:
		cart = cart
		cart.total = 0
		for item in cart.cartitem_set.all():
			cart.total += item.total
			cart.save()

	request.session['cart_items'] = len(cart.cartitem_set.all())

	return render_to_response('cart/view.html', locals(), context_instance=RequestContext(request))

def checkout(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = False

	amount = int(cart.total) * 100

	if request.method == 'POST':
		token = request.POST['stripeToken']

		stripe.Charge.create(
			amount = amount,
			currency = "USD",
			card = token,
			description = "Payment for Cart"
		)

	return render_to_response('cart/checkout.html', locals(), context_instance=RequestContext(request))	

