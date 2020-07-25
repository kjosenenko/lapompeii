from rest_framework import serializers
from .models import MenuCategories

class MenuCategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuCategories
		fields = ('id', 'name', 'description', 'price')