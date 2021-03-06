from django.db import models
from django.utils import timezone


TYPE_CHOICES = (
    ("watches", "watches"),
    ("clothes", "clothes"),
    ("shoes", "shoes"),
    ("events", "events"),
)


class Product(models.Model):
    product_name = models.CharField(max_length=254, default='')
    product_type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
        default="shoes")
    description = models.TextField(null=True)
    more_info = models.TextField(null=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)                                    
    image = models.ImageField(upload_to="product_images", blank=True, null=True)

    def __str__(self):
        return self.product_name


class SKU(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="skus")
    size = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return "%s (size %s)" % (self.product.product_name, self.size)