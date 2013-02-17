from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = ('',
    url(r'', include('tickets.urls'), name='tickets'),
)
