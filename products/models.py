from django.db import models

class ProductManager(models.Manager):
	def all(self):
		return super(ProductManager, self).filter(active=True).exclude(price=None).exclude(price=None)

	def custom_all(self):
		return super(ProductManager, self).filter(active=True).exclude(price=None).exclude(price=None).exclude(description='')

class Product(models.Model):
	title = models.CharField(max_length=220)
	description = models.CharField(max_length=3000, null=True, blank=True)
	price = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = ProductManager()

	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['title']

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	description = models.CharField(max_length=3000, null=True, blank=True)
	image = models.ImageField(upload_to='product/images')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return str(self.image)




