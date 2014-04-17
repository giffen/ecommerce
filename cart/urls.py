from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

# needed to have permission in VirutalEnv
admin.autodiscover()

urlpatterns = patterns('cart.views',
    url(r'^add$', 'add_to_cart'),
    url(r'^view$', 'view', name='view_cart'),
    
)