from rest_framework import serializers
from ..leader.models import Leader


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'
