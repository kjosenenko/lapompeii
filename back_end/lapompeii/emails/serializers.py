from rest_framework import serializers
from .models import Emails

class EmailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Emails
		fields = ('id', 'name', 'email', 'comment', 'phone')