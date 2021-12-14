from django.db import models
from hackaton.apps.locations.models import Country


class Bank(models.Model):
    """ Bancos 
    """
    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.code}: {self.name}'

    class Meta:
        db_table = "bank"


class CompensationBox(models.Model):
    """ Cajas de Compensación 
    """
    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.code}: {self.name}'

    class Meta:
        db_table = "compensation_box"


class Mutual(models.Model):
    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.code}: {self.name}'

    class Meta:
        db_table = "mutual"
