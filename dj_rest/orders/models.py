from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.
from items.models import Item


class SalesOrder(models.Model):
    '''Our sales order model. like in Amazon'''

    item = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, default='No name')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    publish_date = models.DateTimeField(default=now)
    rating = models.FloatField(default=0)
    category = models.CharField(max_length=50, default='No category')
    availability = models.BooleanField(default=True)
    description = models.CharField(max_length=600, default='No description')
    num_reviews = models.PositiveIntegerField(default=0)
    prime_eligible = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(default=0, null=True, blank=True)
    color = models.CharField(max_length=100, default='no color')
    size = models.CharField(max_length=10, default='no size')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-publish_date']  # default ordering by publish date (newest first)
