from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

# needed to have permission in VirutalEnv
admin.autodiscover()

urlpatterns = patterns('',
   # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^contact/', 'contact.views.contact_us', name='contact_us'),
    url(r'^$', 'contact.views.home', name='new_home'),
    url(r'^checkout/', 'cart.views.checkout', name='checkout'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)