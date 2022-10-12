from django.db import models


# Create your models here.
class FeederData(models.Model):
    total_amount_of_feed = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    feed_per_hen = models.DecimalField(default=70.00, max_digits=20, decimal_places=2)
    number_of_chicken = models.IntegerField(default=100)
    feeder_opened = models.BooleanField(default=False)
    # amount_of_feeds_refill = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    @property
    def amount_released(self):
        return "%.2f" % (float(self.feed_per_hen) * float(self.number_of_chicken))

    @property
    def remaining_feed(self):
        return "%.2f" % (float(self.total_amount_of_feed) - float(self.amount_released))

    # @property
    # def feeder_refill(self):
    #     return "%.2f" % (float(self.remaining_feed) + float(self.amount_of_feeds_refill))
