from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cctest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include('main.urls', namespace = "main")),
    url(r'^admin/', include(admin.site.urls)),
)


