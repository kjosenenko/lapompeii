from django.conf.urls import url

from text_areas.views import text_areas as textAreasEndpoint
from text_areas.views import text_area as textAreaEndpoint

urlpatterns = [
    url(r'text_areas/$', textAreasEndpoint),
    url(r'text_areas/(?P<id>\d+)/$', textAreaEndpoint),
]