from django.contrib import admin

from hackaton.apps.business.models import AccountingAccount, Company, CompanyType, CostCenter, Gratification, PaymentMobilization, Sucursal, Unions


class PaymentMobilizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class GratificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_rut', 'updated_at')


class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'updated_at')


class UnionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'rut', 'company', 'updated_at')


class AccountingAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'updated_at')


class SucursalAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'updated_at')


admin.site.register(Company, CompanyAdmin)
admin.site.register(PaymentMobilization, PaymentMobilizationAdmin)
admin.site.register(Gratification, GratificationAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)
admin.site.register(CostCenter, CostCenterAdmin)
admin.site.register(Unions, UnionsAdmin)
admin.site.register(AccountingAccount, AccountingAccountAdmin)
admin.site.register(Sucursal, SucursalAdmin)
