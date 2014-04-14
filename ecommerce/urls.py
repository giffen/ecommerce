from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

# needed to have permissionin VirutalEnv
admin.autodiscover()

urlpatterns = patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',{
				'document_root': settings.STATIC_ROOT
			}),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
				'document_root': settings.MEDIA_ROOT
			}),
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
