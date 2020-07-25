from rest_framework import serializers
from .models import MenuTags

class MenuTagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuTags
		fields = ('id', 'name')