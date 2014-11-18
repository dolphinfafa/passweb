from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^main/$','encryption.views.main'),
	url(r'^code/$','encryption.views.code'),
	url(r'^decode/$','encryption.views.decode'),
)
