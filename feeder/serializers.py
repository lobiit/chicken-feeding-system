from rest_framework import serializers

from .models import FeederData


class FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederData
        fields = [
            'id',
            'feed_per_hen',
            'number_of_chicken',
            'feeder_opened',
        ]


class FeederDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederData
        fields = [
            'id',
            'feed_per_hen',
            'number_of_chicken',
            'feeder_opened',
            'total_amount_of_feed',
        ]


class FeederRefillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederData
        fields = [
            'amount_of_feeds_refill'
        ]
        hidden_fields = ['total_amount_of_feed']