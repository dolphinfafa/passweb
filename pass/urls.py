from django.conf.urls import patterns, include, url
from mainpage import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/$','encryption.views.main'),
                       url(r'^code/$','encryption.views.code'),
                       url(r'^decode/$','encryption.views.decode'),
                       url(r'^$',views.index, name='index'),
)
