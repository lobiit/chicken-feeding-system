from rest_framework import serializers

from .models import Feeder


class Feeder(serializers.ModelSerializer):
    class Meta:
        model = Feeder
        fields = ['feed_per_hen', 'number_of_chicken', 'feeder_opened', 'amount_released', 'remaining_feed']
