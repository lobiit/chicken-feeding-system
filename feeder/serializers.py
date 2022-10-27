from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import FeederData


class FeederSerializer(serializers.ModelSerializer):
    refill_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='feeder-detail',
        lookup_field='pk'
    )

    class Meta:
        model = FeederData
        fields = [
            'url',
            'refill_url',
            'id',
            'feed_per_hen',
            'number_of_chicken',
            'feeder_opened',
        ]

    def get_refill_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("feeder-refill", kwargs={"pk": obj.pk}, request=request)


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
