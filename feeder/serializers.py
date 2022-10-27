from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import FeederData


class FeederSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FeederData
        fields = [
            'url',
            'id',
            'feed_per_hen',
            'number_of_chicken',
            'feeder_opened',
        ]

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("feeder-detail", kwargs={"pk": obj.pk}, request=request)


class FeederDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederData
        fields = [
            'id',
            'feed_per_hen',
            'number_of_chicken',
            'feeder_opened',
            'total_amount_of_feed'
        ]


class FeederRefillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederData
        fields = [
            'amount_of_feeds_refill',
            'total_available_feed'
        ]
