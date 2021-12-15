from django.contrib import admin
from hackaton.apps.forms.models import Forms


class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'business_name')
    search_fields = ('name', 'email', 'business_name',)
    list_filter = ('created_at',)
    
    
    def get_ordering(self, request):
        return ['id']

admin.site.register(Forms, FormAdmin)