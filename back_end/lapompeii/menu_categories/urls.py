from django.conf.urls import url

from menu_categories.views import categories as MenuCategoriesEndpoint
from menu_categories.views import category as MenuCategoryEndpoint

urlpatterns = [
    url(r'menu_categories/$', MenuCategoriesEndpoint),
    url(r'menu_categories/(?P<id>\d+)/$', MenuCategoryEndpoint),
]