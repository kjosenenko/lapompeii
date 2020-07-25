from rest_framework import serializers
from .models import MenuItems
from menu_tags.models import MenuTags

class MenuItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuItems
		fields = ('id', 'name', 'description', 'price', 'category', 'tags')