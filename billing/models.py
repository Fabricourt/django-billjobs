from django.db import models

class Bill(models.Model):

    bill_date = models.DateField()

class BillLine(models.Model):

    SERVICES_CHOICES = (
            ('FT', 'Full Time'),
            ('PT', 'Part Time'),
            ('MD', 'Mid Time'),
            )

    bill = models.ForeignKey(Bill)
    service = models.CharField(max_length=2, choices=SERVICES_CHOICES,
                               default='FT')
    quantity = models.SmallIntegerField(default=1)

