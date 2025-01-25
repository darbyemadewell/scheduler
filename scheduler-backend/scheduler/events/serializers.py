from rest_framework import serializers
from events.models import Day, Event

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    repeating_days = DaySerializer(read_only=True, many=True)
    
    class Meta:
        model = Event
        fields = '__all__'