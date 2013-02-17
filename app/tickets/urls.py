from django.conf.urls.defaults import *

urlpatterns = patterns('tickets.views',
    url(r'^(?P<ticket_id>)/?$', 'single_ticket', name='single'),
)
