from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^', include('main.urls', namespace="main")),
                       (r'^inplaceeditform/', include('inplaceeditform.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', login, name="login"),
                       url(r'^accounts/logout/$', logout, name="logout",
                           kwargs={"next_page": "main:home"}),
                       ) + static(settings.MEDIA_URL,
                                  document_root=settings.MEDIA_ROOT)
