from django.conf.urls.defaults import *
from django.db import models

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from aplicacao.models import Gasto

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index',
        {'queryset': Gasto.objects.all(), 'date_field': 'data'}),
    # Example:
    # (r'^personal_finances/', include('personal_finances.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
