from django.db import models


# Create your models here.
class Item(models.Model):
    '''item class for watch, pencil, belt, any item(s) to order in shop'''
    brand = models.CharField(max_length=255, default=0)  # Patek Philippe
    model = models.CharField(max_length=255, default=0)  # Chronograph 5170G-010
    movement = models.CharField(max_length=255, default=0)  # Manual/Hand-wound Caliber CH 29-535 PS
    case = models.CharField(max_length=255, default=0)  # 39mm White Gold
    dial = models.CharField(max_length=255, default=0)  # Black
    crystal = models.CharField(max_length=255, default=0)  # Sapphire
    bezel = models.CharField(max_length=255, default=0)  # White Gold
    bracelet = models.CharField(max_length=255, default=0)  # Black Leather Strap
    bracelet_length = models.CharField(max_length=255, default=0)  # Fits up to 8 Inch Wrist
    production_year = models.CharField(max_length=255, default=0)  # Papers Dated 2015
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)  # $81,100 (Discontinued)
    new_retail_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)  # $98,200 (Discontinued)
    description = models.CharField(max_length=600, default=0)
