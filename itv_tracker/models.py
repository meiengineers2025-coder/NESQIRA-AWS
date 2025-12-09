from django.db import models

class Customer(models.Model):
    join_date = models.DateField()
    first_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ltv_projection = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_calculated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Customer #{self.id}"
