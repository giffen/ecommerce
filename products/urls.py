from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

# needed to have permission in VirutalEnv
admin.autodiscover()

urlpatterns = patterns('products.views',
    url(r'^$', 'all_products', name="products"),
    url(r'^(?P<slug>.*)/$','single_product'),
)