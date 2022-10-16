from django.db import models


# Create your models here.
class FeederData(models.Model):
    total_amount_of_feed = models.FloatField(default=0, blank=True)
    feed_per_hen = models.DecimalField(default=70.00, max_digits=20, decimal_places=2)
    number_of_chicken = models.IntegerField(default=100)
    feeder_opened = models.BooleanField(default=False)
    amount_of_feeds_refill = models.FloatField(default=0, blank=True)

    @property
    def total_available_feed(self):
        return "%.2f" % (float(self.total_amount_of_feed) + float(self.amount_of_feeds_refill))

    def save(self, *args, **kwargs):
        self.total_amount_of_feed = self.total_available_feed
        super(FeederData, self).save(*args, **kwargs)
