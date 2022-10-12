import time

import schedule as schedule
from django.contrib import messages
from rest_framework import generics, authentication
from rest_framework.decorators import api_view
from .models import FeederData
from .serializers import FeederSerializer


class FeederListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer

    def perform_create(self, serializer):
        total_amount_of_feed = serializer.validated_data.get('total_amount_of_feed') or None
        feed_refill = serializer.validated_data.get('feeder_refill') or None

        if feed_refill is not None:
            total_amount_of_feed += feed_refill
            total_amount_of_feed.save()
        serializer.save()


feeder_list_create_view = FeederListCreateAPIView.as_view()


class FeederDetailView(generics.RetrieveAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer
    # lookup_field = pk


feeder_detail_view = FeederDetailView.as_view()


class FeederUpdateAPIView(generics.UpdateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer

    lookup_field = 'pk'

    def perform_update(self, serializer):
        total_amount_of_feed = serializer.validated_data.get('total_amount_of_feed') or None
        feed_refill = serializer.validated_data.get('feeder_refill') or None

        if feed_refill is not None:
            total_amount_of_feed += feed_refill
            total_amount_of_feed.save()

        instance = serializer.save()


feeder_update_view = FeederUpdateAPIView.as_view()


class FeederDeleteAPIView(generics.DestroyAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


feeder_delete_view = FeederDeleteAPIView.as_view()


def task(request):
    number_of_chicken = FeederData.objects.get('number_of_chicken')
    feed_per_hen = FeederData.objects.get('feeder_per_hen')
    feed_mass = number_of_chicken * feed_per_hen
    total_feed = FeederData.objects.get('total_amount_of_feed')
    refill = FeederData.objects.get('amount_of_feeds_refill')

    feeder_opened = FeederData.objects.get('feeder_opened')

    if total_feed > feed_mass:
        feeder_opened = True
        total_feed -= feed_mass
        messages.success(request, 'feed released into the feeders')
    else:
        messages.error(request, 'Feed depleted, refilling')
        total_feed += refill


schedule.every().day.at("09:00").do(task)

schedule.every().day.at("17:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
