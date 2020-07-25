from django.conf.urls import url

from menu_tags.views import tags as MenuTagsEndpoint
from menu_tags.views import tag as MenuTagEndpoint

urlpatterns = [
    url(r'menu_tags/$', MenuTagsEndpoint),
    url(r'menu_tags/(?P<id>\d+)/$', MenuTagEndpoint),
]