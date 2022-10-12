from rest_framework import serializers

from .models import FeederData


class FeederSerializer(serializers.ModelSerializer):
    amount_released = serializers.SerializerMethodField(read_only=True)
    remaining_feed = serializers.SerializerMethodField(read_only=True)
    # feeder_refill = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FeederData
        fields = ['feed_per_hen',
                  'number_of_chicken',
                  'feeder_opened',
                  'amount_of_feeds_refill',
                  'amount_released',
                  # 'remaining_feed',
                  # 'feeder_refill'
                  ]
