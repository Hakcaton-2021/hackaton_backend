from django.contrib import admin

from hackaton.apps.central.models import Bank, CompensationBox, Mutual

class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'updated_at')


admin.site.register(Bank, BankAdmin)

class CompensationBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'updated_at')


admin.site.register(CompensationBox, CompensationBoxAdmin)

class MutualAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'updated_at')


admin.site.register(Mutual, MutualAdmin)