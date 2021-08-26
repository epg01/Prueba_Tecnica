from django.db import models

# Create your models here.
class Records(models.Model):

    VendorName =  models.TextField()
    FiscalNumber = models.TextField()
    ContractNumbe = models.TextField()
    StartDate = models.TextField()
    EndDate = models.TextField()
    CommPph = models.TextField()


    def __str__(self):
        return self.VendorName