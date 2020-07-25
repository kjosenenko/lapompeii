from django.conf.urls import url

from emails.views import emails as EmailsEndpoint
from emails.views import email as EmailEndpoint

urlpatterns = [
    url(r'emails/$', EmailsEndpoint),
    url(r'emails/(?P<id>\d+)/$', EmailEndpoint),
]