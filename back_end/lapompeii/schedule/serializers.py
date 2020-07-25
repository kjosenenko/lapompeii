from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ('id', 'location', 'description', 'start_date', 'start_time', 'end_date', 'end_time')