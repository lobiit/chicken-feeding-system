from django.contrib import messages
from django.http import request
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import FeederData
from .serializers import FeederSerializer, FeederRefillSerializer, FeederDetailSerializer


class FeederListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer


feeder_list_create_view = FeederListCreateAPIView.as_view()


class FeederRefillAPIView(generics.UpdateAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederRefillSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        # amount_of_feeds = instance.amount_of_feeds_refill + float(instance.total_available_feed)
        # instance.total_amount_of_feed = amount_of_feeds
        # instance = serializer.save(amount_of_feeds_refill=amount_of_feeds_refill,
        #                            total_amount_of_feed=total_amount_of_feed)


feeder_refill_view = FeederRefillAPIView.as_view()


class FeederDetailView(generics.RetrieveAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederDetailSerializer
    lookup_field = 'pk'

    # def show_message(self, message):
    #     obj = FeederData.objects.filter(id=self.lookup_field)
    #
    #     if obj.total_amount_of_feed <= 30000:
    #         messages.error(request, "please refill " + str(obj.id) + "....feeds are running low")
    #


feeder_detail_view = FeederDetailView.as_view()


class FeederDeleteAPIView(generics.DestroyAPIView):
    queryset = FeederData.objects.all()
    serializer_class = FeederSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


feeder_delete_view = FeederDeleteAPIView.as_view()
