from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['nickname', 'address1', 'address2', 'city', 'state', 'postal_code', 'country']
