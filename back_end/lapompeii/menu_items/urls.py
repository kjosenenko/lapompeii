
from django.conf.urls import url

from menu_items.views import items as itemsEndpoint
from menu_items.views import item as itemEndpoint
from menu_items.views import itemsByCategory as itemCategoryEndpoint


urlpatterns = [

    url(r'menu_items/$', itemsEndpoint),
    url(r'menu_items/(?P<id>\d+)/$', itemEndpoint),
    url(r'menu_items/menucategories/(?P<menucategories_id>\d+)/$', itemCategoryEndpoint),
]