from django.contrib import admin

from hackaton.apps.business.models import Company, CompanyType, Gratification, PaymentMobilization


class PaymentMobilizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class GratificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'updated_at')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_rut', 'updated_at')


admin.site.register(Company, CompanyAdmin)
admin.site.register(PaymentMobilization, PaymentMobilizationAdmin)
admin.site.register(Gratification, GratificationAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)
