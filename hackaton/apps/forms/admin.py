from django.contrib import admin
from hackaton.apps.forms.models import Forms

class FormsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'business_name', 'updated_at')


admin.site.register(Forms, FormsAdmin)
