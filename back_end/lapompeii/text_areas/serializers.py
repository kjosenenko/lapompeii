from rest_framework import serializers
from .models import TextAreas

class TextAreasSerializer(serializers.ModelSerializer):
	class Meta:
		model = TextAreas
		fields = ('id', 'title', 'textArea')