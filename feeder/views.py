from rest_framework import generics
from rest_framework.decorators import api_view
from .models import FeederData
from .serializers import FeederSerializer, FeederRefillSerializer, FeederDetailSerializer


class FeederListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer

    def perform_create(self, serializer):
        serializer.save()


feeder_list_create_view = FeederListCreateAPIView.as_view()


class FeederDetailView(generics.RetrieveAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederDetailSerializer
    lookup_field = 'pk'


feeder_detail_view = FeederDetailView.as_view()


class FeederRefillAPIView(generics.UpdateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederRefillSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.total_amount_of_feed and instance.amount_of_feeds_refill and instance.total_amount_of_feed != 0 and instance.amount_of_feeds_refill != 0:
            instance.total_amount_of_feed += instance.amount_of_feeds_refill
            # instance = serializer.save(amount_of_feeds_refill=amount_of_feeds_refill,
            #                            total_amount_of_feed=total_amount_of_feed)


feeder_refill_view = FeederRefillAPIView.as_view()


class FeederDeleteAPIView(generics.DestroyAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


feeder_delete_view = FeederDeleteAPIView.as_view()
