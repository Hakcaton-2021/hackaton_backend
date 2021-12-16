from django.db import models

from hackaton.apps.central.models import Bank, Mutual
from hackaton.apps.forms.models import Forms
from hackaton.apps.locations.models import Comuna, Country


class PaymentMobilization(models.Model):
    """Pago Movilización y Colación"""

    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "payment_mobilization"
        verbose_name = "Pago Movilización y Colación"
        verbose_name_plural = "Pagos Movilización"


class Gratification(models.Model):
    """Pago Gratificación"""

    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "gratification"
        verbose_name = "Pago Gratificación"
        verbose_name_plural = "Pagos Gratificación"



class CompanyType(models.Model):
    """Tipo de Razón Social"""

    code = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "company_type"
        verbose_name = "Tipo de Compañia"
        verbose_name_plural = "Tipos de Compañias"



class Company(models.Model):
    """Razón Social"""

    business_rut = models.CharField(max_length=100, db_index=True)
    business_name = models.CharField(max_length=300)
    business_giro = models.CharField(max_length=600)
    business_direction = models.CharField(max_length=600)
    business_phone = models.CharField(max_length=50)
    representative_name = models.CharField(max_length=300)
    representative_rut = models.CharField(max_length=100, db_index=True)
    representative_email = models.EmailField(max_length=250, db_index=True)
    billing_rut = models.CharField(max_length=100, db_index=True)
    type = models.ForeignKey(CompanyType, on_delete=models.PROTECT)
    form = models.ForeignKey(Forms, on_delete=models.PROTECT)
    gratification = models.ForeignKey(Gratification, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=1)
    mutual = models.ForeignKey(Mutual, on_delete=models.PROTECT)
    mutual_amount = models.FloatField(default=0)
    parent = models.IntegerField(default=None, db_index=True, null=True)
    checking_account = models.IntegerField(default=None, db_index=True, null=True)
    checking_bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    payment_mobilization = models.ForeignKey(
        PaymentMobilization, on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.business_rut}: {self.business_name}"

    class Meta:
        db_table = "company"
        verbose_name = "Compañia"
        verbose_name_plural = "Compañias"



class CostCenter(models.Model):
    """Centro de Costo"""

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100, db_index=True)
    parent = models.IntegerField(default=None, db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "cost_center"
        verbose_name = "Centro de Costo"
        verbose_name_plural = "Centros de Costos"



class Unions(models.Model):
    """Sindicatos"""

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100, db_index=True)
    rut = models.CharField(max_length=100, db_index=True)
    active = models.BooleanField(db_index=True, default=True)
    exempt_amount = models.FloatField(default=0)
    exempt_amount_currency = models.CharField(max_length=10, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "unions"
        verbose_name = "Sindicato"
        verbose_name_plural = "Sindicatos"



class AccountingAccount(models.Model):
    """Cuenta Contable"""

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "accounting_account"
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Cuentas Contables"


class Sucursal(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100, db_index=True)
    number = models.IntegerField(default=0, db_index=True, null=True)
    department = models.CharField(max_length=300)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    range = models.CharField(max_length=200)
    active = models.BooleanField(db_index=True, default=True)
    exempt_amount = models.FloatField(default=0)
    exempt_amount_currency = models.CharField(max_length=10, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        db_table = "sucursal"
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

