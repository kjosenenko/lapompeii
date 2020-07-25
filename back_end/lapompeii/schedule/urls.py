from django.conf.urls import url

from schedule.views import schedule as schduleEndpoint
from schedule.views import event as eventEndpoint

urlpatterns = [
    url(r'schedule/$', schduleEndpoint),
    url(r'schedule/(?P<id>\d+)/$', eventEndpoint),
]