from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello, get_busline

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/', hello),
	url(r'^get_busline/', get_busline),
)
